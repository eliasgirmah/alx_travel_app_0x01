# 🧳 alx_travel_app_0x01

A Django REST Framework-based API for managing travel listings and bookings. This is a backend service built as part of the ALX backend project.

## 📌 Features

- CRUD operations for **Listings**
- CRUD operations for **Bookings**
- Django REST Framework `ModelViewSet`
- API Documentation with **Swagger** and **Redoc**
- SQLite for development database

---

## 🗂️ Project Structure

alx_travel_app_0x01/
│
├── alx_travel_app/ # Django project
│ ├── settings.py
│ ├── urls.py # Includes Swagger and app URLs
│
├── listings/ # Django app
│ ├── models.py # Listing & Booking models
│ ├── views.py # ViewSets
│ ├── serializers.py # DRF serializers
│ ├── urls.py # DRF router
│
├── manage.py
└── README.md # This file

yaml
Copy
Edit

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/eliasgirmah/alx_travel_app_0x01.git
cd alx_travel_app_0x01
2. Set up a virtual environment
bash
Copy
Edit
python -m venv venv
source venv/Scripts/activate  # Windows
# or
source venv/bin/activate      # macOS/Linux
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
If you don’t have requirements.txt, manually install:

bash
Copy
Edit
pip install django djangorestframework drf-yasg
4. Apply migrations
bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
5. Run the server
bash
Copy
Edit
python manage.py runserver
Visit: http://127.0.0.1:8000/

🔁 API Endpoints
Method	Endpoint	Description
GET	/api/listings/	List all listings
POST	/api/listings/	Create a new listing
GET	/api/listings/<id>/	Retrieve listing details
PUT	/api/listings/<id>/	Update a listing
DELETE	/api/listings/<id>/	Delete a listing
GET	/api/bookings/	List all bookings
POST	/api/bookings/	Create a new booking

📘 API Documentation
Swagger: http://127.0.0.1:8000/swagger/

Redoc: http://127.0.0.1:8000/redoc/

🧑‍💻 Authors
Elias Girma