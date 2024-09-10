# **Django Python Machine Test**

## **Task Overview**

This project is a Django-based API that manages `Client` and `Project` data, allowing you to create, list, update, and delete records for both entities. Built using Django REST Framework (DRF), it provides secured RESTful API endpoints, with authentication to protect resources.

---

## **Features**

- **Client Management**: Create, retrieve, update, and delete client records.
- **Project Management**: Associate projects with specific clients, and manage project records.
- **RESTful APIs**: Standard HTTP methods (GET, POST, PUT, DELETE) for interacting with resources.
- **Authentication**: Secured API endpoints with user authentication.

---

## **Folder Structure**

The project is structured as follows:

```bash
├── NimapInfotech/
│   ├── __init__.py          # Package initialization
│   ├── asgi.py              # ASGI config
│   ├── settings.py          # Project settings
│   ├── urls.py              # Root URL configurations
│   ├── wsgi.py              # WSGI config
│
├── project/
│   ├── __init__.py          # Package initialization
│   ├── admin.py             # Admin panel configurations
│   ├── apps.py              # App configurations
│   ├── models.py            # Models for Client and Project
│   ├── serializers.py       # Serializers for converting model data to JSON
│   ├── tests.py             # Test cases for API testing
│   ├── urls.py              # URL patterns for the API
│   ├── views.py             # API views for handling requests
│
├── manage.py                # Django management script
├── db.sqlite3               # SQLite database file
└── README.md                # Project documentation
```

---

## **API Endpoints**

### **Client API**
- `GET /clients/` : List all clients.
- `POST /clients/` : Create a new client.
- `GET /clients/<int:pk>/` : Retrieve a client by ID.
- `PUT /clients/<int:pk>/` : Update a client by ID.
- `DELETE /clients/<int:pk>/` : Delete a client by ID.

### **Project API**
- `GET /clients/<int:client_id>/projects/` : List projects under a specific client.
- `POST /clients/<int:client_id>/projects/` : Create a project under a specific client.
- `GET /projects/` : List all projects.
- `GET /projects/<int:pk>/` : Retrieve a project by ID.
- `PUT /projects/<int:pk>/` : Update a project by ID.
- `DELETE /projects/<int:pk>/` : Delete a project by ID.

---

## **Setup Instructions**

1. **Clone the repository:**

    ```bash
    git clone https://github.com/md-ashraf98/django-REST-API-Project.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd NimapInfotech
    ```

3. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run migrations to set up the database:**

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser to access the admin panel:**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

7. **Access the API at:**

    ```
    http://127.0.0.1:8000/clients/
    http://127.0.0.1:8000/projects/
    ```

---

## **Testing**

To run tests, use the following command:

```bash
python manage.py test
