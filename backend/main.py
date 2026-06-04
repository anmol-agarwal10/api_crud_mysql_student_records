from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import the DatabaseConnection class from conn.py
from conn import DatabaseConnection as dbconn

app = FastAPI()
db = dbconn()

# Configure CORS middleware to allow requests from any origin (for development purposes)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Get All Students Records
@app.get("/allstudent")
def all_students():
    details = db.read("SELECT * FROM students")

    # Format to JSON object
    formatted_details = [
        {"id": row[0], "name": row[1], "age": row[2], "course": row[3]}
        for row in details
    ]

    return {"data":formatted_details}

# Create student record
@app.post("/createstudent")
def create_student(name: str, age: int, course: str):
    db.write(f"INSERT INTO students (name, age, course) VALUES ('{name}', {age}, '{course}')")

    # get the last inserted ID and fetch the created student record
    id_data = db.read("SELECT LAST_INSERT_ID()")[0][0]
    details = db.read(f"SELECT * FROM students where id ={id_data}")[0]

    # Format to JSON object
    formatted_details = [
            {"id": details[0], "name": details[1], "age": details[2], "course": details[3]}
        ]
    
    return {"message": "Student created successfully", "data": formatted_details}

# Get a student record
@app.get("/student/{student_id}")
def get_student(student_id: int):
    details = db.read(f"SELECT * FROM students where id={student_id}")
    try:
        details = details[0]
    except IndexError:
        return {"message": "Student not found"}

    # Format to JSON object
    formatted_details = [
            {"id": details[0], "name": details[1], "age": details[2], "course": details[3]}
        ]
    
    return {"data": formatted_details}

# Update student record
@app.post("/student_update/{student_id}")
def student_update(student_id: int,name: str, age: int, course:str):
    db.write(f"UPDATE students SET name = '{name}', age = {age}, course = '{course}' WHERE id = {student_id};")
    details = db.read(f'select * from students where id={student_id}')
    try:
        details = details[0]
    except IndexError:
        return {"message": "Student not found"}

    # Format to JSON object
    formatted_details = [
            {"id": details[0], "name": details[1], "age": details[2], "course": details[3]}
        ]
    
    return {"message":"successly updated", "data":formatted_details}

# Delete student record
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    details = db.read(f"SELECT * FROM students where id={student_id}")
    try:
        details = details[0]
    except IndexError:
        return {"message": "Student not found"}
    
    db.write(f"DELETE FROM students WHERE id = {student_id};")
    return {"message":"successly deleted"}

