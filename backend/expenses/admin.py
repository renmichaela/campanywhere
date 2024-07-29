from django.contrib import admin
from .models import Attendee, Expense, Payment

# Register your models here.
admin.site.register(Attendee, list_display=['__str__', 'year', 'days_attending', 'camping_type'])
admin.site.register(Expense)
admin.site.register(Payment)
