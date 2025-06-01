from django.core.management.base import BaseCommand
from listings.models import Listing
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        sample_titles = [
            "Cozy Cabin", "Modern Apartment", "Beach House", "Mountain Lodge", "Urban Loft"
        ]
        sample_locations = ["Nairobi", "Mombasa", "Kisumu", "Naivasha", "Diani"]

        Listing.objects.all().delete()

        for i in range(10):
            Listing.objects.create(
                title=random.choice(sample_titles),
                description="A beautiful place to stay with comfort and luxury.",
                location=random.choice(sample_locations),
                price_per_night=random.uniform(50, 300),
                available=random.choice([True, False])
            )

        self.stdout.write(self.style.SUCCESS("Successfully seeded 10 listings."))
