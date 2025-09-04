# 🏢 Company Website API

This project is a **Django REST Framework (DRF)** backend for a company website.  
It provides endpoints for managing content such as Home, About, Services, Contact, and Team, with JWT authentication and basic error handling.

---

## ⚙️ Setup & Run Instructions

1. **Clone the repository** (or create a new Django project):
   ```bash
   git clone https://github.com/your-repo/company_website.git
   cd company_website
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional, for Django Admin)**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

---

## 🔑 Authentication

This project uses **JWT Authentication** via `djangorestframework-simplejwt`.

- **Obtain Token**: `POST /api/token/`
- **Refresh Token**: `POST /api/token/refresh/`

Example request:
```json
POST http://127.0.0.1:8000/api/token/
{
  "username": "admin",
  "password": "admin123"
}
```

Example response:
```json
{
  "refresh": "your-refresh-token",
  "access": "your-access-token"
}
```

---

## 📌 API Endpoints Description

### Home & About
- `GET /api/home/` → Get homepage content  
- `GET /api/about/` → Get about page content  

### Services
- `GET /api/services/` → List all services  

### Contact
- `POST /api/contact/` → Submit a contact form  
  Example request:
  ```json
  {
    "name": "John Doe",
    "email": "john@example.com",
    "message": "I am interested in your services."
  }
  ```

  Example response:
  ```json
  {
    "success": "Message sent successfully"
  }
  ```

### Team
- `GET /api/team/` → List all team members  
- `POST /api/team/add/` → Add a new team member (requires authentication)  

  Example request:
  ```json
  {
    "name": "Alice",
    "role": "Developer"
  }
  ```

  Example response:
  ```json
  {
    "id": 1,
    "name": "Alice",
    "role": "Developer"
  }
  ```

---

## ⚠️ Error Handling

Custom error handlers are implemented:

- `404 Not Found` → Returns:
  ```json
  {
    "detail": "Not found"
  }
  ```

- `500 Internal Server Error` → Returns:
  ```json
  {
    "detail": "Internal server error"
  }
  ```

---

## 🧪 Example Requests/Responses via Postman

### GET Services
**Request**:
```
GET http://127.0.0.1:8000/api/services/
```

**Response**:
```json
[
  {
    "id": 1,
    "title": "Web Development",
    "description": "Building modern websites and web apps."
  },
  {
    "id": 2,
    "title": "Mobile Development",
    "description": "Creating mobile applications for Android and iOS."
  }
]
```

### Invalid Endpoint
**Request**:
```
GET http://127.0.0.1:8000/api/invalid/
```

**Response**:
```json
{
  "detail": "Not found"
}
```

---

## 📂 Project Structure
```
company_website/
│── content/         # Home & About app
│── contact/         # Contact form app
│── team/            # Team management app
│── company_website/ # Main project folder
│── manage.py
```

---

## ✅ Features
- Django REST Framework (DRF)
- JWT Authentication
- CORS enabled
- Structured modular apps
- Custom error handling (404 & 500)
