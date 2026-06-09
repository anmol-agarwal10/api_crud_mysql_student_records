Simple Student API CRUD Application

A simple Student Management CRUD application built with FastAPI, MySQL, and a basic HTML/CSS/JavaScript frontend.

Features:
Create Student
Read Student Records
Update Student Details
Delete Student Records
python
FastAPI REST API
MySQL Database using mysql.connector
Simple HTML/CSS/JavaScript Frontend
Deployable to Azure App Service
FastAPI
Azure App Service

Project Structure
backend/
│
├── main.py
├── conn-azure.py
├── conn.py
├── requirements.txt
│
frontend/
│   └── index.html
└── Azure-Process-Steps.txt
└── README.md

Database Setup:

CREATE DATABASE studentdb;
USE studentdb;
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    age INT
);

Install Dependencies:

pip install -r requirements.txt
requirements.txt
fastapi
uvicorn
mysql-connector-python
Run Application
uvicorn app:app --reload

Application:

http://localhost:8000

API Docs:

http://localhost:80
