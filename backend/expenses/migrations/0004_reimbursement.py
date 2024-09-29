# Generated by Django 5.0.7 on 2024-09-29 22:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0003_attendee_festival_virgin_alter_payment_attendee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reimbursement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('attendee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expenses.attendee')),
            ],
        ),
    ]