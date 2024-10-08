from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from decimal import Decimal
import importlib
from .camping_types import CampingType

CAMPING_TYPES = [
	('ELECTRIC', 'Electric'),
	('PRIMITIVE', 'Primitive')
]

EXPENSE_TYPES = [
	('ELECTRIC', 'Electric'),
	('CAMPING', 'Camping')
]
	
class Attendee(models.Model):
	# default the year field to the current year
	year = models.IntegerField(default=2024)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	days_attending = models.IntegerField()
	camping_type = models.CharField(max_length=50,choices=CAMPING_TYPES)
	festival_virgin = models.BooleanField(default=False)

	def __str__(self):
		return self.user.first_name or self.user.get_short_name()
	
	def camping_expense_share_weight(self):
		if self.festival_virgin:
			return 0.00
		else:
			total_days = Attendee.objects.filter(festival_virgin=False).aggregate(Sum('days_attending'))['days_attending__sum']
			return Decimal(self.days_attending / total_days)
	
	def electric_expense_share_weight(self):
		if self.festival_virgin:
			return 0.00
		else:
			days_of_same_type = Attendee.objects.filter(festival_virgin=False).filter(camping_type=self.camping_type).aggregate(Sum('days_attending'))['days_attending__sum']
			return Decimal(self.days_attending / days_of_same_type)
	
	def share_of_camping_expenses(self):
		if self.festival_virgin:
			return 0.00
		else:
			camping_expenses_sum = Expense.objects.filter(type='CAMPING').aggregate(Sum('amount'))['amount__sum'] or 0
			return round(self.camping_expense_share_weight() * camping_expenses_sum, 2)
	
	def share_of_paid_camping_expenses(self):
		if self.festival_virgin:
			return 0.00
		else:
			paid_expenses_sum = Expense.objects.filter(type='CAMPING').filter(paid_by__isnull=False).aggregate(Sum('amount'))['amount__sum'] or 0
			return round(self.camping_expense_share_weight() * paid_expenses_sum, 2)
	
	def share_of_electric_expenses(self):
		if self.festival_virgin:
			return 0.00
		else:
			camping_type_module = importlib.import_module('expenses.camping_types')
			camping_type_class = getattr(camping_type_module, self.camping_type.capitalize() + 'Camping')
			camping_type = camping_type_class()
			expenses = Expense.objects.filter(type='ELECTRIC')
			expenses_sum = sum([expense.cost(camping_type) for expense in expenses]) or 0
			return round(self.electric_expense_share_weight() * expenses_sum, 2)
	
	def share_of_paid_electric_expenses(self):
		if self.festival_virgin:
			return 0.00
		else:
			camping_type_module = importlib.import_module('expenses.camping_types')
			camping_type_class = getattr(camping_type_module, self.camping_type.capitalize() + 'Camping')
			camping_type = camping_type_class()
			paid_expenses = Expense.objects.filter(type='ELECTRIC').filter(paid_by__isnull=False)
			paid_expenses_sum = sum([expense.cost(camping_type) for expense in paid_expenses]) or 0
			return round(self.electric_expense_share_weight() * paid_expenses_sum, 2)

	def running_total_owed(self):
		if self.festival_virgin:
			return 0.00
		else:
			return round(self.share_of_paid_camping_expenses() + self.share_of_paid_electric_expenses(), 2)
	
	def projected_total_owed(self):
		if self.festival_virgin:
			return 0.00
		else:
			return round(self.share_of_camping_expenses() + self.share_of_electric_expenses(), 2)
		
	# Total of all expenses paid by this attendee
	def group_costs_paid(self):
		return round(sum([expense.amount for expense in self.expenses.all()]), 2)
	
	def total_payments_made(self):
		return round(sum([payment.amount for payment in self.payments.all()]), 2)

	def total_reimbursed(self):
		return round(sum([reimbursement.amount for reimbursement in self.reimbursements.all()]), 2)

	def outstanding_balance(self):
		return round(self.running_total_owed() - self.group_costs_paid() - self.total_payments_made() + self.total_reimbursed(), 2)

# Create your models here.
class Expense(models.Model):
	name = models.CharField(max_length=255)
	type = models.CharField(max_length=50,choices=EXPENSE_TYPES,default='CAMPING')
	amount = models.DecimalField(max_digits=10, decimal_places=2)
	date = models.DateField()
	description = models.TextField(null=True, blank=True)
	paid_by = models.ForeignKey(Attendee, on_delete=models.CASCADE, null=True, blank=True, related_name='expenses')
	
	def __str__(self):
		return self.name
	
	def cost(self, camping_type: CampingType):
		if self.type == 'CAMPING':
			return self.amount
		elif self.type == 'ELECTRIC':
			return self.amount * camping_type.get_weight()
		
	def type_label(self):
		return dict(EXPENSE_TYPES)[self.type]
	
class Payment(models.Model):
	attendee = models.ForeignKey(Attendee, on_delete=models.CASCADE, related_name='payments')
	amount = models.DecimalField(max_digits=10, decimal_places=2)
	date = models.DateField()
	description = models.CharField(max_length=255, null=True, blank=True)
	
	def __str__(self):
		return self.attendee.user.first_name or self.attendee.user.get_short_name()

class Reimbursement(models.Model):
	attendee = models.ForeignKey(Attendee, on_delete=models.CASCADE, related_name='reimbursements')
	amount = models.DecimalField(max_digits=10, decimal_places=2)
	date = models.DateField()
	description = models.CharField(max_length=255, null=True, blank=True)
	
	def __str__(self):
		return self.attendee.user.first_name or self.attendee.user.get_short_name()
