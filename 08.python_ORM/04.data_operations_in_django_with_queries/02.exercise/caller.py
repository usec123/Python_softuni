import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import *

def create_pet(name: str, species: str):
    Pet.objects.create(name=name,species=species)
    return f"{name} is a very cute {species}!"

def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool):
    Artifact.objects.create(name=name,origin=origin,age=age,description=description,is_magical=is_magical)
    return f"The artifact {name} is {age} years old!"

def rename_artifact(artifact: Artifact, new_name: str):
    if artifact.is_magical and artifact.age > 250:
        artifact.name = new_name
        artifact.save()

def delete_all_artifacts():
    Artifact.objects.all().delete()
    
def show_all_locations() -> str:
    return '\n'.join([f'{l.name} has a population of {l.population}!' for l in Location.objects.all().order_by('id')[::-1]])

def new_capital() -> None:
    first_location = Location.objects.first()
    first_location.is_capital = True
    first_location.save()

def get_capitals():
    return Location.objects.all().filter(is_capital=True).values('name')

def delete_first_location():
    Location.objects.first().delete()
    
def apply_discount():
    for car in Car.objects.all():
        car.price_with_discount = car.price - car.price * (sum([int(d) for d in str(car.year)]))/100
        car.save()
    
def get_recent_cars():
    return Car.objects.filter(year__gt=2020).values('model', 'price_with_discount')

def delete_last_car():
    Car.objects.last().delete()
    
def show_unfinished_tasks() -> str:
    return '\n'.join([
        f'Task - {t.title} needs to be done until {t.due_date}!'
            for t in Task.objects.filter(is_finished=False)])

def complete_odd_tasks() -> None:
    for task in Task.objects.all():
        if task.id % 2 == 1:
            task.is_finished = True
            task.save()

def encode_and_replace(text: str, task_title: str):
    text = ''.join(chr(ord(x)-3) for x in text)
    tasks = Task.objects.filter(title=task_title)
    for task in tasks:
        task.description = text
    Task.objects.bulk_update(tasks, ['description'])
    
def get_deluxe_rooms():
    return '\n'.join(f'Deluxe room with number {room.room_number} costs {room.price_per_night}$ per night!'
                     for room in HotelRoom.objects.filter(room_type='Deluxe')
                     if room.id%2==0)

def increase_room_capacity():
    rooms = HotelRoom.objects.all().order_by('id')
    prev_room_capacity = None
    
    for room in rooms:
        if not room.is_reserved:
            continue
        
        if prev_room_capacity is not None:
            room.capacity += prev_room_capacity
        else:
            room.capacity += room.id
        
        prev_room_capacity = room.capacity
    
    HotelRoom.objects.bulk_update(rooms, ['capacity'])

def reserve_first_room():
    room = HotelRoom.objects.all().order_by('room_number')[0]
    room.is_reserved = True
    room.save()
    
def delete_last_room():
    room = HotelRoom.objects.last()
    if not room.is_reserved:
        room.delete()

def update_characters():
    for character in Character.objects.all():
        if character.class_name == 'Mage':
            character.level += 3
            character.intelligence -= 7
        elif character.class_name == 'Warrior':
            character.hit_points //= 2
            character.dexterity += 4
        else:
            character.inventory = 'The inventory is empty'
        character.save()

def fuse_characters(first_character: Character, second_character: Character):
    Character.objects.create(
        name = f'{first_character.name} {second_character.name}',
        class_name = 'Fusion',
        level = (first_character.level + second_character.level) // 2,
        strength = (first_character.strength + second_character.strength) * 1.2,
        dexterity = (first_character.dexterity + second_character.dexterity) * 1.4,
        intelligence = (first_character.intelligence + second_character.intelligence) * 1.5,
        hit_points = first_character.hit_points + second_character.hit_points,
        inventory = "Bow of the Elven Lords, Amulet of Eternal Wisdom"
            if first_character.class_name in ('Mage', 'Scout') else
            "Dragon Scale Armor, Excalibur"
    )
    first_character.delete()
    second_character.delete()

def grand_dexterity():
    characters = Character.objects.all()
    for character in characters:
        character.dexterity = 30
    Character.objects.bulk_update(characters, ['dexterity'])

def grand_intelligence():
    characters = Character.objects.all()
    for character in characters:
        character.intelligence = 40
    Character.objects.bulk_update(characters, ['intelligence'])

def grand_strength():
    characters = Character.objects.all()
    for character in characters:
        character.strength = 50
    Character.objects.bulk_update(characters, ['strength'])

def delete_characters():
    Character.objects.filter(inventory='The inventory is empty').delete()

# Create queries within functions

# [print(create_pet(name,species)) for name,species in zip(
#     ['Buddy', 'Whiskers', 'Rocky'],
#     ['Dog', 'Cat', 'Hamster']
# )]

# print(create_artifact('Ancient Sword', 'Lost Kingdom', 500, 'A legendary sword with a rich history', True))
# artifact_object = Artifact.objects.get(name='Ancient Sword')
# rename_artifact(artifact_object, 'Ancient Shield')
# print(artifact_object.name)

# for name, region, population, description, is_capital in zip(
#     ['Sofia', 'Plovdiv', 'Varna'],
#     ['Sofia Region', 'Plovdiv Region', 'Varna Region'],
#     [1329000, 346942, 330486],
#     ['The capital of Bulgaria and the largest city in the country', 'The second-largest city in Bulgaria with a rich historical heritage', 'A city known for its sea breeze and beautiful beaches on the Black Sea'],
#     [False, False, False]
# ):
#     location = Location()
#     location.name = name
#     location.region = region
#     location.population = population
#     location.description = description
#     location.is_capital = is_capital
#     location.save()

# print(show_all_locations())
# print(new_capital())
# print(get_capitals())

# for model, year, color, price in zip(
#     ['Mercedes C63 AMG', 'Audi Q7 S line', 'Chevrolet Corvette'],
#     [2019, 2023, 2021],
#     ['white', 'black', 'dark grey'],
#     [120_000, 183_900, 199_999],
# ):
#     car = Car()
#     car.model = model
#     car.year = year
#     car.color = color
#     car.price = price
#     car.save()

# apply_discount()
# print(get_recent_cars())

# Task.objects.create(
#     title='Sample Task',
#     description='This is a sample task description',
#     due_date='2023-10-31',
#     is_finished=False
# )
# encode_and_replace("Zdvk#wkh#glvkhv$", "Sample Task")
# print(Task.objects.get(title='Sample Task').description)

# for room_number, room_type, capacity, amenities, price_per_night in zip(
#     [401, 501, 601],
#     ['Standard', 'Deluxe', 'Deluxe'],
#     [2, 3, 6],
#     ['Tv', 'Wi-Fi', 'Jacuzzi'],
#     [100, 200, 400]
# ):
#     room = HotelRoom()
#     room.room_number = room_number
#     room.room_type = room_type
#     room.capacity = capacity
#     room.amenities = amenities
#     room.price_per_night = price_per_night
#     room.save()

# print(get_deluxe_rooms())
# reserve_first_room()
# print(HotelRoom.objects.get(room_number=401).is_reserved)

# character1 = Character.objects.create(
#     name='Gandalf',
#     class_name='Mage',
#     level=10,
#     strength=15,
#     dexterity=20,
#     intelligence=25,
#     hit_points=100,
#     inventory='Staff of Magic, Spellbook',
#     )

# character2 = Character.objects.create(
#     name='Hector',
#     class_name='Warrior',
#     level=12,strength=30,
#     dexterity=15,
#     intelligence=10,
#     hit_points=150,
#     inventory='Sword of Troy, Shield of Protection',
#     )

# fuse_characters(character1, character2)
# fusion = Character.objects.filter(class_name='Fusion').get()
# print(fusion.name)
# print(fusion.class_name)
# print(fusion.level)
# print(fusion.intelligence)
# print(fusion.inventory)
