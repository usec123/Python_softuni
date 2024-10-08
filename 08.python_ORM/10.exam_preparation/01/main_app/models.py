from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from main_app.managers import DirectorManager


# Create your models here.
class Person(models.Model):
    full_name = models.CharField(
        max_length=120,
        validators=[
            MinLengthValidator(2),
        ],
        )
    
    birth_date = models.DateField(default='1900-01-01')
    
    nationality = models.CharField(
        max_length=50,
        default='Unknown',
        )
    
    class Meta:
        abstract=True
        

class AwardedMixin(models.Model):
    is_awarded = models.BooleanField(default=False)
    
    class Meta:
        abstract=True
    

class LastUpdatedMixin(models.Model):
    last_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract=True


class Director(Person):
    years_of_experience = models.SmallIntegerField(
        validators=[
            MinValueValidator(0),
        ],
        default=0,
    )
    
    objects = DirectorManager()
    

class Actor(Person, AwardedMixin, LastUpdatedMixin):
    pass
    
class Movie(AwardedMixin, LastUpdatedMixin):
    class GenreChoices(models.TextChoices):
        ACTION = 'Action', 'Action'
        COMEDY = 'Comedy', 'Comedy'
        DRAMA = 'Drama', 'Drama'
        OTHER = 'Other', 'Other'
    
    
    title = models.CharField(
        max_length=150,
        validators=[
            MinLengthValidator(5),
        ],
        )
    
    release_date = models.DateField()
    
    storyline = models.TextField(null=True, blank=True)
    
    genre = models.CharField(
        max_length=6,
        choices=GenreChoices.choices,
        default=GenreChoices.OTHER,
        )
    
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10),
        ],
        default=0,
        )
    
    is_classic = models.BooleanField(default=False)
    
    director = models.ForeignKey(
        to=Director,
        on_delete=models.CASCADE,
        related_name='director_movies'
    )
    
    starring_actor = models.ForeignKey(
        to=Actor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='starring_movies'
    )
    
    actors = models.ManyToManyField(
        to=Actor,
        related_name='actors_movies'
        )
    