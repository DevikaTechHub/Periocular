# Periocular Based Unique ID Generation

A Django project for periocular-based unique ID generation and certificate/application management.

## Technologies

- Python
- Django
- MySQL
- HTML, CSS, JavaScript

## Setup

1. Install dependencies.
2. Create a MySQL database named `certificate`.
3. Set environment variables for local secrets:

```bash
DJANGO_SECRET_KEY=your-secret-key
DB_NAME=certificate
DB_USER=root
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=3306
```

4. Run migrations:

```bash
python manage.py migrate
```

5. Start the server:

```bash
python manage.py runserver
```
