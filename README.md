# Hotel Room Booking System

A simple Django REST Framework (DRF) project for managing hotel room bookings.

---

## Features

### Admin Endpoints
1. **View All Rooms**: `GET /api/admin/rooms/`
2. **Add a New Room**: `POST /api/admin/rooms/`
3. **Update Room Details**: `PUT /api/admin/rooms/<room_id>/`
4. **Delete a Room**: `DELETE /api/admin/rooms/<room_id>/`

### User Endpoints
1. **Search Available Rooms**: `GET /api/rooms/`
2. **Book a Room**: `POST /api/rooms/book/`
3. **Cancel Booking**: `DELETE /api/rooms/cancel/`

---

## Installation Guide

### Prerequisites
- Python 3.10+
- Virtual Environment (optional but recommended)
- MySQL/PostgreSQL or SQLite (default)

### Steps

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd <project-directory>
   cd backend
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Database**
   - Update `backend/settings.py` for your database.
   - By default, MYSQL is used. To use any other RDBMS, add your database credentials:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': '<db_name>',
             'USER': '<db_user>',
             'PASSWORD': '<db_password>',
             'HOST': 'localhost',
             'PORT': '5432',
         }
     }
     ```

5. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create Superuser (for Admin Access)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the Development Server**
   ```bash
   python manage.py runserver
   ```
   Access the app at `http://127.0.0.1:8000/`

---

## Project Structure

```
backend/
├── app/
│   ├── admin.py         # Admin panel configuration
│   ├── models.py        # Database models for Room and Booking
│   ├── serializers.py   # DRF serializers for validation and serialization
│   ├── views.py         # API views for admin and user endpoints
│   ├── urls.py          # URL routing for app endpoints
├── reservations/
│   ├── settings.py      # Project settings
│   ├── urls.py          # Root URL configuration
│   ├── wsgi.py          # WSGI entry point
├── manage.py            # Django's management script
```

---
