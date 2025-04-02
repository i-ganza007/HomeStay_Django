# Listings/management/commands/script.py
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from ...models import PropertyListing
from lorem_text import lorem

User = get_user_model()  

class Command(BaseCommand):
    help = 'Populate Property Listings'

    def handle(self, *args, **kwargs):
        all_users = list(User.objects.all())

        if len(all_users) < 4:
            self.stdout.write(self.style.ERROR('Not enough users found in the database.'))
            return

        # Sample property listings
        pros = [
            ['La Casa', 2000000, lorem.sentence(), 'Kigali', 'KK424', True, all_users[0], 333, 3, 2, False],
            ['La Frontier', 492902942, lorem.sentence(), 'Kigali', 'KK424', True, all_users[1], 333, 3, 2, False],
            ['La Monsieur', 53424324, lorem.sentence(), 'Kigali', 'KK424', True, all_users[2], 333, 3, 2, True],
            ['La Fraud', 24324, lorem.sentence(), 'Kigali', 'KK424', True, all_users[3], 333, 3, 2, True],
            ['La fmdsfl', 413224342, lorem.sentence(), 'Kigali', 'KK424', True, all_users[2], 2313122, 3, 2, True],
            ['La Ibala', 809808070, lorem.sentence(), 'Kigali', 'KK424', True, all_users[0], 2313122, 3, 2, False],
            ['La Ilingi', 13333334324, lorem.sentence(), 'Kigali', 'KK424', True, all_users[3], 333, 3, 2, False],
        ]

        property_listings = []
        for prop in pros:
            property_listing = PropertyListing(
                prop_name=prop[0],
                price=prop[1],
                description=prop[2],
                location=prop[3],
                address=prop[4],
                is_urban=prop[5],
                owner=prop[6],  
                potential_interest=prop[7],
                bedrooms=prop[8],
                bathrooms=prop[9],
                is_furnished=prop[10]
            )
            property_listings.append(property_listing)

        PropertyListing.objects.bulk_create(property_listings)
        self.stdout.write(self.style.SUCCESS('Successfully populated property listings.'))