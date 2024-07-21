from decimal import Decimal
from django.db import models
from django.db.models import Q, Count, F, Avg


class RealEstateListingManager(models.Manager):
    def by_property_type(self, property_type: str):
        return self.filter(property_type=property_type)
    
    def in_price_range(self, min_price: Decimal, max_price: Decimal):
        query = Q(price__gte=min_price) & Q(price__lte=max_price)
        return self.filter(query)

    def with_bedrooms(self, bedrooms_count: int):
        query = Q(bedrooms=bedrooms_count)
        return self.filter(query)
    
    def popular_locations(self):
        # return self.order_by(F(Count('id')))
        return self.values('location').annotate(location_count=Count('id')).order_by('-location_count', 'location')[:2:]


class VideoGameManager(models.Manager):
    def games_by_genre(self, genre: str):
        return self.filter(genre=genre)
    
    def recently_released_games(self, year: int):
        return self.filter(release_year__gte=year)

    def highest_rated_game(self):
        return self.order_by('-rating').first()

    def lowest_rated_game(self):
        return self.order_by('rating').first()
    
    def average_rating(self):
        return f'{self.aggregate(avg=Avg("rating"))["avg"]:.1f}'
