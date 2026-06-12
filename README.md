# Django Blog Application

A simple Blog Application built using Django that allows users to register, log in, create blog posts, and manage their own content.

---

## Features

### Authentication
- User Registration (Signup)
- User Login
- User Logout

### Blog Management
- Create New Blog Posts
- View All Blog Posts
- View User-Specific Posts
- Author-Based Post Ownership

### UI
- Template Inheritance using `base.html`
- Static Images and Styling
- Responsive Navigation

---

## Tech Stack

- Python
- Django
- SQLite
- HTML
- CSS

---

## Project Structure

```text
django-blog/
│
├── blog/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── migrations/
│
├── django_blog/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── templates/
│   └── blog/
│       ├── base.html
│       ├── home.html
│       ├── login.html
│       ├── signup.html
│       ├── newpost.html
│       └── mypost.html
│
├── static/
│   └── image/
│       ├── logo.png
│       └── pho.png
│
├── manage.py
└── db.sqlite3
```

---

## Database Models

### Posts

| Field | Type |
|---------|---------|
| title | CharField |
| content | TextField |
| author | ForeignKey(User) |
| created_at | DateTimeField |

---

## Application Workflow

### User Registration

```text
Signup
   ↓
Create User
   ↓
Redirect to Login
```

### User Login

```text
Login
   ↓
Authenticate User
   ↓
Redirect to Home
```

### Create Blog Post

```text
Logged In User
   ↓
Create Post
   ↓
Save Author Automatically
   ↓
Display on Home Page
```

### My Posts

```text
Current User
   ↓
Filter Posts by Author
   ↓
Display User's Posts
```

---

## Concepts Practiced

### Django Fundamentals
- Models
- Views
- URL Routing
- Templates
- Static Files

### Authentication
- Django User Model
- Authentication System
- Login/Logout Handling

### Database Operations
- Create Records
- Retrieve Records
- Filter Records
- Foreign Key Relationships

### Frontend
- HTML Templates
- Template Inheritance
- Static Assets

---

## Installation

Clone the repository

```bash
git clone https://github.com/Anjali470/django-blog.git
```

Move into project directory

```bash
cd django-blog
```

Create virtual environment

```bash
python -m venv venv
```

Activate environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install django
```

Run migrations

```bash
python manage.py migrate
```

Create superuser (optional)

```bash
python manage.py createsuperuser
```

Start development server

```bash
python manage.py runserver
```

Open browser

```text
http://127.0.0.1:8000
```

---

## Future Enhancements

- Edit Post
- Delete Post
- User Profile Page
- Rich Text Editor
- Post Categories
- Comments System
- Likes and Reactions
- Django REST Framework APIs
- PostgreSQL Integration

---

## Author

**Anjali Kumara**

GitHub:
https://github.com/Anjali470