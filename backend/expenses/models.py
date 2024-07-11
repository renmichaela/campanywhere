from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Expense(models.Model):
	name = models.CharField(max_length=255)
	amount = models.DecimalField(max_digits=10, decimal_places=2)
	date = models.DateField()
	description = models.TextField(null=True, blank=True)
	paid_by = models.ForeignKey(User, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.name
	
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
		return self.user.get_username()