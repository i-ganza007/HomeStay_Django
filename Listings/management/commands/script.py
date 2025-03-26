from django.core.management.base import BaseCommand

from ...models import PropertyListing 
from lorem_text import lorem

class Command(BaseCommand):
    help = 'Populate Property Listings'

    def handle(self, *args, **kwargs):
        pros = [
            ['La Casa', 2000000, lorem.sentence(), 'Kigali', 'KK424', True, 333, 3, 2, False],
            ['La Frontier', 492902942, lorem.sentence(), 'Kigali', 'KK424', True, 333, 3, 2, False],
            ['La Monsieur', 53424324, lorem.sentence(), 'Kigali', 'KK424', True, 333, 3, 2, True],
            ['La Fraud', 24324, lorem.sentence(), 'Kigali', 'KK424', True, 333, 3, 2, True],
            ['La fmdsfl', 413224342, lorem.sentence(), 'Kigali', 'KK424', True, 2313122, 3, 2, True],
            ['La Ibala', 809808070, lorem.sentence(), 'Kigali', 'KK424', True, 2313122, 3, 2, False],
            ['La Ilingi', 13333334324, lorem.sentence(), 'Kigali', 'KK424', True, 333, 3, 2, False],
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
                potential_interest=prop[6],
                bedrooms=prop[7],
                bathrooms=prop[8],
                is_furnished=prop[9]
            )
            property_listings.append(property_listing)

        PropertyListing.objects.bulk_create(property_listings)
        self.stdout.write(self.style.SUCCESS('Successfully populated property listings.'))