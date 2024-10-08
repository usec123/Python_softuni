from datetime import date, timedelta
from typing import Any
from django.db import models
from django.forms import ValidationError


class BooleanChoiceField(models.BooleanField):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs['choices'] = ((True, 'Available'),
                             (False, 'Not Available'))
        kwargs['default'] = True
        super().__init__(*args, **kwargs)
    

# Create your models here.
class Animal(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    birth_date = models.DateField()
    sound = models.CharField(max_length=100)
    
    @property
    def age(self):
        return (date.today() - self.birth_date).days // 365
        # return (date.today() - timedelta(self.birth_date)).year


class Mammal(Animal):
    fur_color = models.CharField(max_length=50)


class Bird(Animal):
    wing_span = models.DecimalField(max_digits=5, decimal_places=2)


class Reptile(Animal):
    scale_type = models.CharField(max_length=50)


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    
    class Meta:
        abstract = True


class ZooKeeper(Employee):
    class SpecialtyChoices(models.TextChoices):
        MAMMALS = ('Mammals', 'Mammals')
        BIRDS = ('Birds', 'Birds')
        REPTILES = ('Reptiles', 'Reptiles')
        OTHERS = ('Others', 'Others')
    
    
    specialty = models.CharField(max_length=10, choices=SpecialtyChoices.choices)
    managed_animals = models.ManyToManyField(to=Animal)
    
    def clean(self):
        if self.specialty not in self.SpecialtyChoices:
            raise ValidationError('Specialty must be a valid choice.')


class Veterinarian(Employee):
    license_number = models.CharField(max_length=10)
    availability = BooleanChoiceField()


class ZooDisplayAnimal(Animal):
    def display_info(self):
        return f'Meet {self.name}! Species: {self.species}, born {self.birth_date}. It makes a noise like \'{self.sound}\'.'
    
    def is_endangered(self):
        return f'{self.species} is ' + \
                ('not ' if self.species not in ("Cross River Gorilla", "Orangutan", "Green Turtle") else '') + \
                    'at risk.'
    
    class Meta:
        proxy = True


