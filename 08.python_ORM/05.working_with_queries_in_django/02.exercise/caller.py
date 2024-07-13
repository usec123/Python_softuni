import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from main_app.models import *

# Create and check models
def show_highest_rated_art() -> str:
    top = ArtworkGallery.objects.order_by('-rating', 'id').first()
    return f'{top.art_name} is the highest-rated art with a {top.rating} rating!'

def bulk_create_arts(first_art: ArtworkGallery, second_art: ArtworkGallery):
    ArtworkGallery.objects.bulk_create([first_art, second_art])

def delete_negative_rated_arts():
    ArtworkGallery.objects.filter(rating__lt=0).delete()

def show_the_most_expensive_laptop() -> str:
    laptop = Laptop.objects.order_by('-price', '-id').first()
    return f'{laptop.brand} is the most expensive laptop available for {laptop.price}$!'

def bulk_create_laptops(args):
    Laptop.objects.bulk_create(args)

def update_to_512_GB_storage():
    Laptop.objects.filter(brand__in=('Asus', 'Lenovo')).update(storage=512)

def update_to_16_GB_memory():
    Laptop.objects.filter(brand__in=('Apple', 'Dell', 'Acer')).update(memory=16)

def update_operation_systems():
    Laptop.objects.filter(brand='Asus').update(operation_system=OSChoices.WINDOWS)
    Laptop.objects.filter(brand='Apple').update(operation_system=OSChoices.MACOS)
    Laptop.objects.filter(brand__in=('Dell', 'Acer')).update(operation_system=OSChoices.LINUX)
    Laptop.objects.filter(brand='Lenovo').update(operation_system=OSChoices.CHROME_OS)

def delete_inexpensive_laptops():
    Laptop.objects.filter(price__lt=1200).delete()

def bulk_create_chess_players(args):
    ChessPlayer.objects.bulk_create(args)

def delete_chess_players():
    ChessPlayer.objects.filter(title='no title').delete()

def change_chess_games_won():
    ChessPlayer.objects.filter(title='GM').update(games_won=30)

def change_chess_games_lost():
    ChessPlayer.objects.filter(title='no title').update(games_lost=25)

def change_chess_games_drawn():
    ChessPlayer.objects.all().update(games_drawn=10)

def grand_chess_title_GM():
    ChessPlayer.objects.filter(rating__gte=2400).update(title='GM')

def grand_chess_title_IM():
    ChessPlayer.objects.filter(rating__range=(2300, 2399)).update(title='IM')
    
def grand_chess_title_FM():
    ChessPlayer.objects.filter(rating__range=(2200, 2299)).update(title='FM')
    
def grand_chess_title_regular_player():
    ChessPlayer.objects.filter(rating__range=(0, 2199)).update(title='regular player')
    
def set_new_chefs():
    Meal.objects.filter(meal_type='Breakfast').update(chef='Gordon Ramsay')
    Meal.objects.filter(meal_type='Lunch').update(chef='Julia Child')
    Meal.objects.filter(meal_type='Dinner').update(chef='Jamie Oliver')
    Meal.objects.filter(meal_type='Snack').update(chef='Thomas Keller')

def set_new_preparation_times():
    Meal.objects.filter(meal_type='Breakfast').update(preparation_time='10 minutes')
    Meal.objects.filter(meal_type='Lunch').update(preparation_time='12 minutes')
    Meal.objects.filter(meal_type='Dinner').update(preparation_time='15 minutes')
    Meal.objects.filter(meal_type='Snack').update(preparation_time='5 minutes')
    
def update_low_calorie_meals():
    Meal.objects.filter(meal_type__in=('Breakfast', 'Dinner')).update(calories=400)

def update_high_calorie_meals():
    Meal.objects.filter(meal_type__in=('Lunch', 'Snack')).update(calories=700)
    
def delete_lunch_and_snack_meals():
    Meal.objects.filter(meal_type__in=('Lunch', 'Snack')).delete()

def show_hard_dungeons():
    return '\n'.join(f'{dungeon.name} is guarded by {dungeon.boss_name} who has {dungeon.boss_health} health points!' for dungeon in Dungeon.objects.filter(difficulty='Hard').order_by('-location'))

def bulk_create_dungeons(args):
    Dungeon.objects.bulk_create(args)

def update_dungeon_names():
    Dungeon.objects.filter(difficulty='Easy').update(name='The Erased Thombs')
    Dungeon.objects.filter(difficulty='Medium').update(name='The Coral Labyrinth')
    Dungeon.objects.filter(difficulty='Hard').update(name='The Lost Haunt')

def update_dungeon_bosses_health():
    Dungeon.objects.exclude(difficulty='Easy').update(boss_health=500)
    
def update_dungeon_recommended_levels():
    Dungeon.objects.filter(difficulty='Easy').update(recommended_level=25)
    Dungeon.objects.filter(difficulty='Medium').update(recommended_level=50)
    Dungeon.objects.filter(difficulty='Hard').update(recommended_level=75)

def update_dungeon_rewards():
    Dungeon.objects.filter(boss_health=500).update(reward='1000 Gold')
    Dungeon.objects.filter(location__startswith='E').update(reward='New dungeon unlocked')
    Dungeon.objects.filter(location__endswith='s').update(reward='Dragonheart Amulet')
    
def set_new_locations():
    Dungeon.objects.filter(recommended_level=25).update(location='Enchanted Maze')
    Dungeon.objects.filter(recommended_level=50).update(location='Grimstone Mines')
    Dungeon.objects.filter(recommended_level=75).update(location='Shadowed Abyss')
    
def show_workouts():
    return '\n'.join(
        f'{workout.name} from {workout.workout_type} type has {workout.difficulty} difficulty!'
        for workout in Workout.objects.filter(workout_type__in=('Calisthenics', 'CrossFit')).order_by('id'))
    
def get_high_difficulty_cardio_workouts():
    return Workout.objects.filter(workout_type='Cardio', difficulty='High').order_by('instructor')

def set_new_instructors():
    Workout.objects.filter(workout_type='Cardio').update(instructor='John Smith')
    Workout.objects.filter(workout_type='Strength').update(instructor='Michael Williams')
    Workout.objects.filter(workout_type='Yoga').update(instructor='Emily Johnson')
    Workout.objects.filter(workout_type='CrossFit').update(instructor='Sarah Davis')
    Workout.objects.filter(workout_type='Calisthenics').update(instructor='Chris Heria')
    
def set_new_duration_times():
    Workout.objects.filter(instructor='John Smith').update(duration='15 minutes')
    Workout.objects.filter(instructor='Sarah Davis').update(duration='30 minutes')
    Workout.objects.filter(instructor='Chris Heria').update(duration='45 minutes')
    Workout.objects.filter(instructor='Michael Williams').update(duration='1 hour')
    Workout.objects.filter(instructor='Emily Johnson').update(duration='1 hour and 30 minutes')
    
def delete_workouts():
    Workout.objects.exclude(workout_type__in=('Strength', 'Calisthenics')).delete()
    

# Run and print your queries
# artwork1 = ArtworkGallery(artist_name='Vincent van Gogh', art_name='Starry Night', rating=4, price=1200000.0)
# artwork2 = ArtworkGallery(artist_name='Leonardo da Vinci', art_name='Mona Lisa', rating=5, price=1500000.0)
# Bulk saves the instances
# bulk_create_arts(artwork1, artwork2)
# print(show_highest_rated_art())
# print(ArtworkGallery.objects.all())

# laptop1 = Laptop(brand='Asus',processor='Intel Core i5',memory=8, storage=256, operation_system='MacOS', price=899.99 )
# laptop2 = Laptop( brand='Apple', processor='Chrome OS', memory=16, storage=256, operation_system='MacOS', price=1399.99 )
# laptop3 = Laptop( brand='Lenovo', processor='AMD Ryzen 7', memory=12, storage=256, operation_system='Linux', price=999.99, )

# # # Create a list of instances
# laptops_to_create = [laptop1, laptop2, laptop3]

# # # Use bulk_create to save the instances
# bulk_create_laptops(laptops_to_create)
# update_to_512_GB_storage()
# update_operation_systems()

# # # Retrieve 2 laptops from the database
# asus_laptop = Laptop.objects.filter(brand__exact='Asus').get()
# lenovo_laptop = Laptop.objects.filter(brand__exact='Lenovo').get()
# print(asus_laptop.storage)
# print(lenovo_laptop.operation_system)

# meal1 = Meal.objects.create(
#     name="Pancakes",
#     meal_type="Breakfast",
#     preparation_time="20 minutes",
#     difficulty=3,
#     calories=350,
#     chef="Jane",
#     )

# meal2 = Meal.objects.create(
#     name="Spaghetti Bolognese",
#     meal_type="Dinner",
#     preparation_time="45 minutes",
#     difficulty=4,
#     calories=550,
#     chef="Sarah",
#     )

# # Test the set_new_chefs function
# set_new_chefs()

# # Test the set_new_preparation_times function
# set_new_preparation_times()

# # Refreshes the instances
# meal1.refresh_from_db()
# meal2.refresh_from_db()

# # Print the updated meal information
# print("Meal 1 Chef:", meal1.chef)
# print("Meal 1 Preparation Time:", meal1.preparation_time)
# print("Meal 2 Chef:", meal2.chef)
# print("Meal 2 Preparation Time:", meal2.preparation_time)

# # Create two instances
# dungeon1 = Dungeon(
#     name="Dungeon 1",
#     boss_name="Boss 1",
#     boss_health=1000,
#     recommended_level=75,
#     reward="Gold",
#     location="Eternal Hell",
#     difficulty="Hard",
#     )

# dungeon2 = Dungeon(
#     name="Dungeon 2",
#     boss_name="Boss 2",
#     boss_health=400,
#     recommended_level=25,
#     reward="Experience",
#     location="Crystal Caverns",
#     difficulty="Easy",
#     )
# # Bulk save the instances
# bulk_create_dungeons([dungeon1, dungeon2])
# # Update boss's health
# update_dungeon_bosses_health()
# # Show hard dungeons
# hard_dungeons_info = show_hard_dungeons()
# print(hard_dungeons_info)
# # Change dungeon names based on difficulty
# update_dungeon_names()
# dungeons = Dungeon.objects.order_by('boss_health')
# print(dungeons[0].name)
# print(dungeons[1].name)
# # Change the dungeon rewards
# update_dungeon_rewards()
# dungeons = Dungeon.objects.order_by('boss_health')
# print(dungeons[0].reward)
# print(dungeons[1].reward)

# Create two Workout instances
# workout1 = Workout.objects.create(
#     name="Push-Ups",
#     workout_type="Calisthenics",
#     duration="10 minutes",
#     difficulty="Intermediate",
#     calories_burned=200,
#     instructor="Bob"
#     )

# workout2 = Workout.objects.create(
#     name="Running",
#     workout_type="Cardio",
#     duration="30 minutes",
#     difficulty="High",
#     calories_burned=400,
#     instructor="Lilly"
#     )

# # Run the functions
# print(show_workouts())
# high_difficulty_cardio_workouts = get_high_difficulty_cardio_workouts()
# for workout in high_difficulty_cardio_workouts:
#     print(f"{workout.name} by {workout.instructor}")

# set_new_instructors()
# for workout in Workout.objects.all():
#     print(f"Instructor: {workout.instructor}")

# set_new_duration_times()
# for workout in Workout.objects.all():
#     print(f"Duration: {workout.duration}")
