from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
import decimal
	
class Attendee(models.Model):
	# default the year field to the current year
	year = models.IntegerField(default=2024)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	days_attending = models.IntegerField()
	camping_type = models.CharField(max_length=50,choices=[
		('ELECTRIC', 'Electric'),
		('PRIMITIVE', 'Primitive')
	])

	def __str__(self):
		return self.user.get_short_name()
	
	def expense_share_weight(self):
		total_days = Attendee.objects.aggregate(Sum('days_attending'))['days_attending__sum']
		return self.days_attending / total_days
	
	def electric_expense_share_weight(self):
		days_of_same_type = Attendee.objects.filter(camping_type=self.camping_type).aggregate(Sum('days_attending'))['days_attending__sum']
		return self.days_attending / days_of_same_type
	
	def share_of_paid_expenses(self):
		paid_expenses_sum = Expense.objects.filter(paid_by__isnull=False).aggregate(Sum('amount'))['amount__sum']
		return decimal.Decimal(self.expense_share_weight()) * paid_expenses_sum

# Create your models here.
class Expense(models.Model):
	name = models.CharField(max_length=255)
	amount = models.DecimalField(max_digits=10, decimal_places=2)
	date = models.DateField()
	description = models.TextField(null=True, blank=True)
	paid_by = models.ForeignKey(Attendee, on_delete=models.CASCADE, null=True, blank=True, related_name='expenses')
	
	def __str__(self):
		return self.name