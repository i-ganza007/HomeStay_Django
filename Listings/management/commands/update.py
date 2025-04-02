from Listings.models import PropertyListing
from django.core.management.base import BaseCommand
from Users.models import User

class Command(BaseCommand):
    help = 'Update Listings with appropriate users'

    def handle(self, *args, **options):
        

        all_listings = list(PropertyListing.objects.all())  
        all_users = list(User.objects.all())

        has_owners = []
        user_count = len(all_users)

        for index, listing in enumerate(all_listings):
            listing.owner = all_users[index % user_count]  
            has_owners.append(listing)

        PropertyListing.objects.bulk_update(has_owners, ['owner'])
        self.stdout.write('Updated successfully with owners')