from Student.database import db
from Student.models import Student
from bson import ObjectId

def student_helper(student):
    student["id"] = str(student["_id"])
    del student["_id"]
    return student

async def add_student(student_data: dict):
    student = await db.students.insert_one(student_data)
    new_student = await db.students.find_one({"_id": student.inserted_id})
    return student_helper(new_student)

async def get_student(student_id: str):
    student = await db.students.find_one({"_id": ObjectId(student_id)})
    if student:
        return student_helper(student)
    return None

async def update_student(student_id: str, data: dict):
    student = await db.students.find_one({"_id": ObjectId(student_id)})
    if student:
        updated_student = await db.students.update_one(
            {"_id": ObjectId(student_id)},
            {"$set": data}
        )
        return updated_student.modified_count > 0
    return False

async def delete_student(student_id: str):
    student = await db.students.delete_one({"_id": ObjectId(student_id)})
    return student.deleted_count > 0
