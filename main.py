from fastapi import FastAPI, Query
from pydantic import BaseModel, EmailStr
from pymongo import MongoClient
from typing import Optional

# -----------------------
# FastAPI App Metadata
# -----------------------
app = FastAPI(
    title="Automated Student Attendance System",
    description="""
    🚀 **Smart India Hackathon Project**  
    This system manages student attendance with real-time analytics.  

    👥 **Team Name**: Hack Forge
    """,
    version="1.0.0"
)

# -----------------------
# MongoDB Atlas Connection
# -----------------------
MONGO_URI = "mongodb+srv://skdb_user:trav90210@clusterproject.gqu1hes.mongodb.net/attendance_db?retryWrites=true&w=majority"
client = MongoClient(MONGO_URI)

db = client["attendance_db"]
students_collection = db["students"]
attendance_collection = db["attendance"]

# -----------------------
# Models
# -----------------------
class Student(BaseModel):
    name: str
    roll_no: str
    department: str
    email: EmailStr   # ✅ Email validation

class Attendance(BaseModel):
    student_id: str
    date: str
    status: str  # "Present" / "Absent"

# -----------------------
# Routes
# -----------------------

@app.get("/", tags=["Home"])
def home():
    return {"message": "Welcome to the Automated Student Attendance System 🚀"}

# ✅ Add Student
@app.post("/students", tags=["Students"])
def add_student(student: Student):
    student_dict = student.dict()
    students_collection.insert_one(student_dict)
    return {"message": "✅ Student added successfully", "student": student_dict}

# 📋 Get All Students (with optional filters)
@app.get("/students", tags=["Students"])
def get_students(
    department: Optional[str] = Query(None, description="Filter by department"),
    roll_no: Optional[str] = Query(None, description="Search by roll number"),
):
    query = {}
    if department:
        query["department"] = department
    if roll_no:
        query["roll_no"] = roll_no

    students = list(students_collection.find(query, {"_id": 0}))
    return {"students": students}

# 📝 Mark Attendance
@app.post("/attendance", tags=["Attendance"])
def mark_attendance(attendance: Attendance):
    attendance_dict = attendance.dict()
    attendance_collection.insert_one(attendance_dict)
    return {"message": "✅ Attendance marked!", "attendance": attendance_dict}

# 📊 Get Attendance Report (for a student)
@app.get("/attendance/report/{roll_no}", tags=["Attendance"])
def get_attendance_report(
    roll_no: str,
    start_date: Optional[str] = Query(None, description="Start date (YYYY-MM-DD)"),
    end_date: Optional[str] = Query(None, description="End date (YYYY-MM-DD)"),
):
    query = {"student_id": roll_no}
    if start_date and end_date:
        query["date"] = {"$gte": start_date, "$lte": end_date}

    total = attendance_collection.count_documents(query)
    present = attendance_collection.count_documents({**query, "status": "Present"})
    
    return {
        "student_id": roll_no,
        "total_days": total,
        "present_days": present,
        "attendance_percentage": f"{(present/total*100) if total > 0 else 0:.2f}%"
    }

# 📊 Get Daily Attendance Analytics
@app.get("/attendance/daily", tags=["Analytics"])
def daily_attendance(date: str = Query(..., description="Date (YYYY-MM-DD)")):
    total = attendance_collection.count_documents({"date": date})
    present = attendance_collection.count_documents({"date": date, "status": "Present"})
    absent = attendance_collection.count_documents({"date": date, "status": "Absent"})

    return {
        "date": date,
        "total_students": total,
        "present": present,
        "absent": absent,
        "attendance_percentage": f"{(present/total*100) if total > 0 else 0:.2f}%"
    }
