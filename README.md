# 📝 Blog Platform with Commenting System

A RESTful Blog Platform built using **Django REST Framework** that allows users to create and manage blog posts, comment on articles, and securely authenticate using Django's authentication system.

## ✨ Features
- **Authentication:** Registration, Login, and Logout (Token Authentication and Password Hashing)
- **Role-Based Access Control:** Author, Reader, and Admin roles utilizing Django Permissions
- **CRUD Operations:** Full management for Blog Posts, Comments, Categories, and Tags via DRF APIs
- **Nested Comments:** Threaded replies on blog posts
- **Search & Filter:** Search by Title, Author, and Category; filter by Tags and Publication Date
- **Pagination:** Clean, paginated responses for post listings
- **API Documentation:** Interactive Swagger UI and ReDoc endpoints
- **Email Notifications:** Automatic emails dispatched on post creation using Django Signals
- **Clean Architecture:** Well-commented and structured source code

## 🛠 Tech Stack

- Python
- Django
- Django REST Framework
- PostgreSQL
- Git & GitHub
- Postman

## 👥 User Roles

| Role | Permissions |
|------|-------------|
| **Author** | Create, update, and delete own blog posts |
| **Reader** | View posts, create comments, and write nested replies |
| **Admin** | Full system access; manage users, roles, and content |

## 📂 Project Structure

```
blog_platform/
├── blog_app/
├── my_project/
├── users/
├── .gitignore
├── manage.py
└── requirements.txt
```



## 🗄 Database Design

The project consists of the following main entities:

- User (custom user with role)
- Profile
- Category
- Tag
- Post
- Comment
- PostTag (junction table)

### Relationships

- One User can create multiple Blog Posts.
- One User can create multiple Comments.
- One Blog Post belongs to one Category.
- One Blog Post can have multiple Tags and One Tag can have multiple Blog Posts.
- One Blog Post can have multiple Comments.
- One comment can have multiple nested comments.


## 📋 Prerequisites

Make sure the following are installed on your system:

- Python 3.10+
- PostgreSQL
- Git
- pip (Python Package Manager)

## ⚙️ Installation



### Clone the Repository

```bash
git clone https://github.com/jilani-code369/blog-platform.git
```

### Navigate to the Project Directory

```bash
cd blog-platform
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Virtual Environment 


```bash
venv\Scripts\activate (Windows)
```

```bash
source venv/Scripts/activate (Git Bash)
```


```bash
source venv/bin/activate  (Linux/macOS)
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Database Migrations

```bash
python manage.py migrate
```

### Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

### Run the Development Server

```bash
python manage.py runserver
```


## 📄 API Endpoints


**Root URL**

[`http://127.0.0.1:8000/`](http://127.0.0.1:8000/)


### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | [`/auth/register/`](http://127.0.0.1:8000/auth/register/) | Register a new user |
| POST | [`/auth/login/`](http://127.0.0.1:8000/auth/login/) | User login |
| POST | [`/auth/logout/`](http://127.0.0.1:8000/auth/logout/) | User logout |
| CRUD | [`/api/v1/user/`](http://127.0.0.1:8000/api/v1/user/) | User management |
| CRUD | [`/api/v1/post/`](http://127.0.0.1:8000/api/v1/post/) | Blog post management |
| CRUD | [`/api/v1/category/`](http://127.0.0.1:8000/api/v1/category/) | Category management |
| CRUD | [`/api/v1/tag/`](http://127.0.0.1:8000/api/v1/tag/) | Tag management |
| CRUD | [`/api/v1/post-tag/`](http://127.0.0.1:8000/api/v1/post-tag/) | Post-tag management |
| CRUD | [`/api/v1/comment/`](http://127.0.0.1:8000/api/v1/comment/) | Comment management |


### Documentation API

| Endpoint | Description |
|----------|-------------|
| [`/api/schema/`](http://127.0.0.1:8000/api/schema/) | OpenAPI Schema |
| [`/api/schema/swagger-ui/`](http://127.0.0.1:8000/api/schema/swagger-ui/) | Swagger UI Documentation |
| [`/api/schema/redoc/`](http://127.0.0.1:8000/api/schema/redoc/) | ReDoc Documentation |



## 🔐 Environment Variables

Create a `.env` file and configure the following variables:

```
SECRET_KEY=your_django_secret_key
DEBUG=True

DB_ENGINE=django.db.backends.postgresql
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432

CORS_ALLOW_ALL_ORIGINS=True

EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST=smtp.gmail.com
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
```

## 🧪 Testing

The APIs were tested using **Postman** to verify:

- Authentication
- Authorization
- CRUD Operations
- Searching
- Filtering
- Pagination
- Error Handling



## 💡 Future Improvements

- JWT Authentication
- Image Upload for Blog Posts
- Like and Bookmark System
- Blog Analytics
- Use Django Groups for Role Based Access



## 👨‍💻 Author

**Jilani Nadaf**

Backend Developer

- [GitHub](https://github.com/jilani-code369/)
- [Email](mailto:nadafjilani182@gmail.com)
- [LinkedIn](https://www.linkedin.com/in/jilani-nadaf)



## 📄 License

This project is developed for educational purposes and internship submission.
