# alx_travel_app_0x00

## Features

- Listings with descriptions, location, price, and images
- Booking system for guests
- Reviews for listings
- Seed script to populate test data

## Setup

```bash
# Create virtual environment
python3 -m venv env
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Seed the database
python manage.py seed
