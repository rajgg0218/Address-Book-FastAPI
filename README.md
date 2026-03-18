# Address Book FastAPI

This project is a minimal Address Book API built with FastAPI and SQLite. The API allows users to create, update, delete, and retrieve addresses. Users can also search for addresses within a specified distance from given coordinates.

The application does not include a GUI. Instead, it uses FastAPI's built-in Swagger documentation to test and interact with the API.

---

# Features

* Create an address
* Update an address
* Delete an address
* Retrieve all addresses
* Retrieve addresses within a given distance and coordinates
* Data validation using Pydantic
* SQLite database storage

---

# Requirements

Before running the application, ensure the following are installed:

* Python 3.9 or newer
* pip (Python package manager)

Check your Python version:

```
python --version
```

---

# 1. Clone the Repository

Clone the repository to your local machine:

```
git clone https://github.com/YOUR_USERNAME/address-book-fastapi.git
```

Navigate to the project folder:

```
cd address-book-fastapi
```

---

# 2. Create a Virtual Environment

Creating a virtual environment is recommended to isolate project dependencies.

## Windows

```
python -m venv venv
venv\\Scripts\\activate
```

## Mac / Linux

```
python3 -m venv venv
source venv/bin/activate
```

After activation you should see `(venv)` at the start of your terminal line.

---

# 3. Install Dependencies

Install all required Python packages:

```
pip install -r requirements.txt
```

Example requirements.txt:

```
fastapi
uvicorn
sqlalchemy
pydantic
```

---

# 4. Run the Application

Start the API server using Uvicorn:

```
uvicorn main:app --reload
```

Expected output:

```
Uvicorn running on http://127.0.0.1:8000
```

The API server is now running.

---

# 5. Open the API Documentation

Open the following URL in your browser:

```
http://127.0.0.1:8000/docs
```

This opens the interactive Swagger UI where you can test the API endpoints.

---

# How to Use the API

## Create an Address

Endpoint:

```
POST /addresses
```

Example request body:

```
{
  "name": "Home",
  "street": "123 Main Street",
  "city": "Manila",
  "latitude": 14.5995,
  "longitude": 120.9842
}
```

---

## Get All Addresses

Endpoint:

```
GET /addresses
```

Returns all saved addresses.

---

## Update an Address

Endpoint:

```
PUT /addresses/{id}
```

Example:

```
PUT /addresses/1
```

Example request body:

```
{
  "name": "Updated Home",
  "street": "456 New Street",
  "city": "Quezon City",
  "latitude": 14.676,
  "longitude": 121.0437
}
```

---

## Delete an Address

Endpoint:

```
DELETE /addresses/{id}
```

Example:

```
DELETE /addresses/1
```

---

## Find Nearby Addresses

Endpoint:

```
GET /addresses/nearby
```

Query parameters:

* latitude
* longitude
* distance_km

Example request:

```
/addresses/nearby?latitude=14.5995&longitude=120.9842&distance_km=5
```

This returns addresses within the specified distance from the given coordinates.

---

# Database

When the application runs for the first time, it automatically creates a local SQLite database file:

```
addresses.db
```

No manual database configuration is required.

---

# Project Structure

```
address-book-fastapi
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── crud.py
├── requirements.txt
└── README.md
```

---

# Stopping the Server

To stop the application server, press:

```
CTRL + C
```

---

# Notes

* The API can be fully tested using the Swagger interface.
* The SQLite database is automatically generated when the application starts.
* No additional configuration is required to run the application.
