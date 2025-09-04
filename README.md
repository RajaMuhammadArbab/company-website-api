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

## EXAMPLE PROJECT-DEMO ##
<img width="1377" height="547" alt="1" src="https://github.com/user-attachments/assets/d5aa3af1-0160-4dae-937c-0839164c6339" />
<img width="1373" height="546" alt="2" src="https://github.com/user-attachments/assets/3a4aaaa1-2eb8-43c8-9a92-e504ff08ac1c" />
<img width="1379" height="866" alt="3" src="https://github.com/user-attachments/assets/17acd9e7-6325-408e-9d9f-61c684afab98" />
<img width="1387" height="569" alt="4" src="https://github.com/user-attachments/assets/30faa587-84b6-43da-80e6-deec6d5580ac" />
<img width="1388" height="755" alt="5" src="https://github.com/user-attachments/assets/53e96806-2f17-4a2f-965a-38ca8dd8c780" />
<img width="1385" height="886" alt="6" src="https://github.com/user-attachments/assets/e9d77034-f726-4f42-bc5e-2458e39ce18e" />
<img width="1395" height="566" alt="7" src="https://github.com/user-attachments/assets/d1344d3a-9aad-4988-89cd-0f9ab85e4d00" />
<img width="1371" height="465" alt="8" src="https://github.com/user-attachments/assets/df582656-532b-4f60-a0f9-51834f5b4209" />
<img width="1382" height="522" alt="9" src="https://github.com/user-attachments/assets/d147a263-3ca6-4ea5-9627-20f3520c75c2" />


