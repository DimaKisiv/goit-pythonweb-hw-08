# 📇 Contacts REST API

A simple REST API built with **FastAPI**, **SQLAlchemy**, and
**PostgreSQL**\
for storing and managing contacts.

## ✨ Features

-   Create, read, update, delete (CRUD) contacts
-   Search by **first name**, **last name**, or **email**
-   Get contacts with birthdays in the next 7 days
-   Validation with **Pydantic**
-   Auto-generated Swagger UI (`/docs`) and ReDoc (`/redoc`)

------------------------------------------------------------------------

## 🛠️ Requirements

-   Python 3.12+
-   PostgreSQL 16+
-   pip

------------------------------------------------------------------------

## 🚀 Run locally

### 1. Create virtual environment

``` bash
python -m venv venv
source venv/bin/activate   # on Linux/Mac
venv\Scripts\activate      # on Windows
```

### 2. Install dependencies

``` bash
pip install -r requirements.txt
```

### 3. Start PostgreSQL

Make sure you have a database running. Example:

``` bash
createdb contactsdb
```

Update `DATABASE_URL` in `.env` or `database.py` if needed.

### 4. Run the API

``` bash
uvicorn main:app --reload
```

Open: - Swagger UI: <http://127.0.0.1:8000/docs>\
- ReDoc: <http://127.0.0.1:8000/redoc>

------------------------------------------------------------------------

## 🐳 Run with Docker Compose

### 1. Start services

``` bash
docker-compose up --build
```

This starts: - PostgreSQL at `localhost:5432` - FastAPI app at
`http://127.0.0.1:8000`

### 2. Stop services

``` bash
docker-compose down
```

------------------------------------------------------------------------

## 📚 API Endpoints

-   **POST** `/contacts/` → Create contact\
-   **GET** `/contacts/` → List contacts\
-   **GET** `/contacts/{id}` → Get contact by ID\
-   **PUT** `/contacts/{id}` → Update contact\
-   **DELETE** `/contacts/{id}` → Delete contact\
-   **GET** `/contacts/search/` → Search contacts\
-   **GET** `/contacts/upcoming_birthdays/` → Birthdays in next 7 days

------------------------------------------------------------------------

## 📄 License

MIT
