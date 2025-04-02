# Remember  
from django.core.management.base import BaseCommand
from datetime import date, time
from ...models import Event
from lorem_text import lorem

class Command(BaseCommand):
    help = 'Creating dummy event listings'

    def handle(self, *args, **options):
        events = [
            [lorem.sentence(), 'World Cup', 10000, 'Arena', 20, date(2025, 10, 14), time(15, 23, 19), time(19, 33, 19)],
            [lorem.sentence(), 'Stanley Cup', 5000, 'Arena', 40, date(2025, 11, 4), time(10, 23, 19), time(12, 23, 19)],
            [lorem.sentence(), 'Grand Prix', 130000, 'Mont Kigali', 10, date(2025, 3, 28), time(23, 23, 19), time(23, 59, 19)],  
            [lorem.sentence(), 'NBA Finals', 50000, 'Mercedes Arena', 220, date(2025, 8, 10), time(12, 23, 19), time(14, 23, 19)],
            [lorem.sentence(), 'Karate', 17000, 'Arena 2', 290, date(2025, 6, 24), time(7, 23, 19), time(15, 0, 0)],
            [lorem.sentence(), 'Kungfu Cup', 40000, 'Arena', 20, date(2025, 6, 2), time(3, 23, 19), time(11, 30, 19)],
            [lorem.sentence(), 'Peace Cup', 600, 'Arena', 20, date(2025, 8, 29), time(18, 23, 19), time(19, 30, 19)],
            [lorem.sentence(), 'Pompo Cup', 10000, 'Arena', 20, date(2025, 6, 24), time(22, 23, 19), time(23, 0, 19)],
            [lorem.sentence(), 'Vienna Cup', 10000, 'Vienna', 20, date(2025, 10, 17), time(15, 23, 19), time(18, 0, 0)]
        ]

        event_objects = []
        for event in events:
            event_instance = Event(
                description=event[0],
                event_name=event[1],
                price=event[2],
                location=event[3],
                slots_available=event[4],
                date=event[5],  
                time_from=event[6],
                time_to=event[7],
            )
            event_objects.append(event_instance)

        Event.objects.bulk_create(event_objects)
        self.stdout.write(self.style.SUCCESS('Successfully populated event listings.'))
