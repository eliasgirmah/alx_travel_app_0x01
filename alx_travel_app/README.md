# 🧳 alx_travel_app_0x01

A Django REST Framework-based API for managing travel listings and bookings. This is a backend service built as part of the **ALX backend project**.

---

## 📌 Features

- ✅ CRUD operations for **Listings**
- ✅ CRUD operations for **Bookings**
- ✅ Built using Django REST Framework `ModelViewSet`
- ✅ API Documentation with **Swagger** and **Redoc**
- ✅ Uses SQLite for the development database

---

## 🗂️ Project Structure

```
alx_travel_app_0x01/
│
├── alx_travel_app/    # Django project settings and URLs
│   ├── settings.py
│   ├── urls.py        # Includes Swagger and app URLs
│
├── listings/          # Listings Django app
│   ├── models.py      # Listing & Booking models
│   ├── views.py       # DRF ViewSets
│   ├── serializers.py # DRF serializers
│   ├── urls.py        # DRF router
│
├── manage.py
└── README.md          # This file
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/eliasgirmah/alx_travel_app_0x01.git
cd alx_travel_app_0x01
```

### 2️⃣ Set Up a Virtual Environment

```bash
# Windows
python -m venv venv
source venv/Scripts/activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, install manually:

```bash
pip install django djangorestframework drf-yasg
```

### 4️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Run the Development Server

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🔁 API Endpoints

| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| GET | `/api/listings/` | List all listings |
| POST | `/api/listings/` | Create a new listing |
| GET | `/api/listings/<id>/` | Retrieve listing details |
| PUT | `/api/listings/<id>/` | Update a listing |
| DELETE | `/api/listings/<id>/` | Delete a listing |
| GET | `/api/bookings/` | List all bookings |
| POST | `/api/bookings/` | Create a new booking |

---

## 📘 API Documentation

- **Swagger:** [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
- **Redoc:** [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

---

## 🧑‍💻 Author

**Elias Girma**
