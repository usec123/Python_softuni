import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Director, Actor, Movie
from django.db.models import Q, F, Count, Avg

# Create queries within functions
# print(Director.objects.get_directors_by_movies_count())

def get_directors(search_name:str|None=None, search_nationality:str|None=None):
    res = ''
    if search_name and search_nationality:
        res = Director.objects.filter(full_name__contains=search_name, nationality__contains=search_nationality)
    
    elif not search_name and not search_nationality:
        res = ''
    
    else:
        if search_name:
            res = Director.objects.filter(full_name__icontains=search_name)
        else:
            res = Director.objects.filter(nationality__icontains=search_nationality)
    
    if res:
        res = res.order_by('full_name')
        return '\n'.join(
            f'Director: {director.full_name}, nationality: {director.nationality}, experience: {director.years_of_experience}' for director in res
        )
    return ''

def get_top_director():
    res = Director.objects.get_directors_by_movies_count().first()
    if res:
        return f"Top Director: {res.full_name}, movies: {res.movies_count}."
    else: return ''

def get_top_actor():
    res = Actor.objects\
            .prefetch_related('starring_movies')\
            .annotate(movies_count = Count('starring_movies'), average_rating = Avg('starring_movies__rating'))\
            .order_by('-movies_count', 'full_name')\
            .first()
    if res:
        if res.movies_count:
            avg = f'{res.average_rating:.1f}'
            return f'Top Actor: {res.full_name}, starring in movies: {", ".join(m.title for m in res.starring_movies.all() if m)}, movies average rating: {avg}'
    return ''

# 
def get_actors_by_movies_count():
    res = Actor.objects\
            .annotate(movies_count=Count('actors_movies'))\
            .order_by('-movies_count', 'full_name')\
            [:3:]

    if not res or not res[0].movies_count:
        return ''
        
    return '\n'.join(
        f'{actor.full_name}, participated in {actor.movies_count} movies' for actor in res
    )
    
def get_top_rated_awarded_movie():
    top_movie = Movie.objects\
        .select_related('starring_actor')\
        .prefetch_related('actors')\
        .filter(is_awarded=True)\
        .order_by('-rating', 'title')\
        .first()
    
    if top_movie is None:
        return ''
    
    s_actor = 'N/A'
    if top_movie.starring_actor:
        s_actor = top_movie.starring_actor.full_name
    
    cast = ', '.join(top_movie.actors.order_by('full_name').values_list('full_name', flat=True))
    
    return (f"Top rated awarded movie: {top_movie.title}, "
            f"rating: {top_movie.rating:.1f}. Starring actor: "
            f"{s_actor}. "
            f"Cast: {cast}.")
    

def increase_rating():
    classic_movies = Movie.objects.filter(is_classic=True, rating__lt=10)
    
    classic_movies.update(rating=F('rating')+0.1)
    
    updated_movies = classic_movies.count()
    return f"Rating increased for {updated_movies} movies." if updated_movies else f'No ratings increased.'
