import os
import django
from django.core.exceptions import ValidationError

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here

# Create queries within functions
# 1
# from main_app.models import Restaurant
# from django.core.exceptions import ValidationError

# valid_restaurant = Restaurant(
#     name="Delicious Bistro",
#     location="123 Main Street",
#     description="A cozy restaurant with a variety of dishes.",
#     rating=5.00,
# )

# try:
#     valid_restaurant.full_clean()
#     valid_restaurant.save()
#     print("Valid Restaurant saved successfully!")
# except ValidationError as e:
#     print(f"Validation Error: {e}")

# invalid_restaurant = Restaurant(
#     name="A",
#     location="A" * 201,
#     description="A restaurant with a long name and invalid rating.",
#     rating=5.01,
# )

# try:
#     invalid_restaurant.full_clean()
#     invalid_restaurant.save()
#     print("Invalid Restaurant saved successfully!")
# except Exception as e:
#     print(f"Validation Error: {e}")

# 2
# from main_app.models import Restaurant, Menu

# # Keep the data from the previous exercise, so you can reuse it

# valid_menu = Menu(
#     name="Menu at The Delicious Bistro",
#     description="** Appetizers: **\nSpinach and Artichoke Dip\n** Main Course: **\nGrilled Salmon\n** Desserts: **\nChocolate Fondue",
#     restaurant=Restaurant.objects.first(),
# )

# try:
#     valid_menu.full_clean()
#     valid_menu.save()
#     print("Valid Menu saved successfully!")
# except ValidationError as e:
#     print(f"Validation Error: {e}")

# invalid_menu = Menu(
#     name="Incomplete Menu",
#     description="** Appetizers: **\nSpinach and Artichoke Dip",
#     restaurant=Restaurant.objects.first(),
# )

# try:
#     invalid_menu.full_clean()
#     invalid_menu.save()
#     print("Invalid Menu saved successfully!")
# except ValidationError as e:
#     print(f"Validation Error: {e}")

# 3
# from main_app.models import Restaurant, RestaurantReview
# from django.core.exceptions import ValidationError

# restaurant1 = Restaurant.objects.create(name="Restaurant A", location="123 Main St.", description="A cozy restaurant", rating=4.88)
# restaurant2 = Restaurant.objects.create(name="Restaurant B", location="456 Elm St.",  description="Charming restaurant", rating=3.59)

# RestaurantReview.objects.create(reviewer_name="Bob", restaurant=restaurant1, review_content="Good experience overall.", rating=4)
# RestaurantReview.objects.create(reviewer_name="Aleks", restaurant=restaurant1, review_content="Great food and service!", rating=5)
# RestaurantReview.objects.create(reviewer_name="Charlie", restaurant=restaurant2, review_content="It was ok!", rating=2)

# duplicate_review = RestaurantReview(reviewer_name="Aleks", restaurant=restaurant1, review_content="Another great meal!", rating=5)

# try:
#     duplicate_review.full_clean()
#     duplicate_review.save()
# except ValidationError as e:
#     print(f"Validation Error: {e}")


# print("All Restaurant Reviews:")
# for review in RestaurantReview.objects.all():
#     print(f"Reviewer: {review.reviewer_name}, Rating: {review.rating}, Restaurant: {review.restaurant.name}")

# 4
# from main_app.models import Restaurant, RegularRestaurantReview, FoodCriticRestaurantReview
# from django.core.exceptions import ValidationError

# restaurant1 = Restaurant.objects.create(name="Restaurant A", location="123 Main St.", description="A cozy restaurant", rating=4.88)
# RegularRestaurantReview.objects.create(reviewer_name="Bob", restaurant=restaurant1, review_content="Good experience overall.", rating=4)
# RegularRestaurantReview.objects.create(reviewer_name="Aleks", restaurant=restaurant1, review_content="Great food and service!", rating=5)

# duplicate_review = RegularRestaurantReview(reviewer_name="Aleks", restaurant=restaurant1, review_content="Another great meal!", rating=5)

# try:
#     duplicate_review.full_clean()
#     duplicate_review.save()
# except ValidationError as e:
#     print(f"Validation Error: {e}")

# print("Regular Restaurant Review:")
# print(f"Model Name: {RegularRestaurantReview._meta.verbose_name}")
# print(f"Model Plural Name: {RegularRestaurantReview._meta.verbose_name_plural}")

# print("Food Critic Restaurant Review:")
# print(f"Model Name: {FoodCriticRestaurantReview._meta.verbose_name}")
# print(f"Model Plural Name: {FoodCriticRestaurantReview._meta.verbose_name_plural}")

# 6
