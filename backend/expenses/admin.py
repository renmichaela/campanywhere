from django.contrib import admin
from .models import Attendee, Expense

# Register your models here.
admin.site.register(Attendee, list_display=['user', 'year', 'days_attending', 'camping_type'])
admin.site.register(Expense)
