from django.core.management.base import BaseCommand
from Users.models import User

class Command(BaseCommand):
    help = 'Create sample users in the db'

    def handle(self, *args, **kwargs):
        users = []

        premier_users = [
            [1, 'Yan', 'Wanza', 'yanwanza4@gmail.com', 'ribuyu10@CSA', 'yanwanza'],
            [2, 'Jox', 'Wetin', 'joxwetin@gmail.com', 'goodboy123', 'joxwetin'],
            [3, 'Levon', 'James', 'levonmes@gmail.com', 'comeon098', 'levonj'],
            [4, 'Chris', 'Brown', 'chrisbr@gmail.com', 'brbrown', 'chrisb']
        ]

        for user in premier_users:
            if not User.objects.filter(email=user[3]).exists():  # Avoid duplicate emails
                inst = User(
                    id=user[0],
                    first_name=user[1],
                    last_name=user[2],
                    email=user[3],
                    password=user[4],  # Note: Password needs to be hashed
                    username=user[5]  # Ensure username is unique
                )
                users.append(inst)

        if users:
            User.objects.bulk_create(users)
            self.stdout.write(self.style.SUCCESS('Successfully populated new users.'))
        else:
            self.stdout.write(self.style.WARNING('No new users were added.'))
