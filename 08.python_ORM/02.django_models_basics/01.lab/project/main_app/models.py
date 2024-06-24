from datetime import date

from django.db import models


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=30)
    email_address = models.EmailField()
    photo = models.URLField()
    birth_date = models.DateField()
    works_full_time = models.BooleanField()
    created_on = models.DateTimeField(auto_now_add=True)


class Department(models.Model):
    # city_choices = [
    #     # first value is the one written in the DB, second one is the one seen by the user
    #     ('Varna', 'Varna'),
    #     ('Plovdiv', 'Plovdiv'),
    #     ('Sofia', 'Sofia'),
    #     ('Burgas', 'Burgas'),
    # ]
    class CityChoices(models.TextChoices):
        SOFIA = 'Sofia', 'Sofia'
        PLOVDIV = 'Plovdiv', 'Plovdiv'
        VARNA = 'Varna', 'Varna'
        BURGAS = 'Burgas', 'Burgas'

    code = models.CharField(max_length=4, primary_key=True, unique=True)
    name = models.CharField(max_length=50, unique=True)
    employees_count = models.PositiveIntegerField(default=1, verbose_name='Employees Count')
    location = models.CharField(max_length=20, null=True, blank=True, choices=CityChoices, default='Varna')
    last_edited_on = models.DateTimeField(auto_now=True, editable=False)


class Project(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    duration_in_days = models.PositiveIntegerField(null=True, blank=True, verbose_name='Duration in Days')
    estimated_hours = models.FloatField(null=True, blank=True, verbose_name='Estimated Hours')
    start_date = models.DateField(verbose_name='Start Date', null=True, blank=True, default=date.today())
    created_on = models.DateTimeField(editable=False, auto_now_add=True)
    last_edited_on = models.DateTimeField(editable=False, auto_now=True)
