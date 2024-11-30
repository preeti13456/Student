from fastapi import FastAPI, HTTPException
from schemas import StudentCreate, StudentResponse
from crud import add_student, get_student, update_student, delete_student

app = FastAPI()

@app.post("/students", response_model=StudentResponse, status_code=201)
async def create_student(student: StudentCreate):
    new_student = await add_student(student.dict())
    return new_student

@app.get("/students/{student_id}", response_model=StudentResponse)
async def read_student(student_id: str):
    student = await get_student(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.put("/students/{student_id}", response_model=StudentResponse)
async def update_student_endpoint(student_id: str, student: StudentCreate):
    updated = await update_student(student_id, student.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="Student not found")
    return {**student.dict(), "id": student_id}

@app.delete("/students/{student_id}", status_code=204)
async def delete_student_endpoint(student_id: str):
    deleted = await delete_student(student_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Student not found")
    
