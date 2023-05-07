from fastapi import FastAPI
# from pydantic import BaseModel
from schema import Course
from database import engine, Base

app = FastAPI()
Base.metadata.create_all(bind=engine)

fakedb = []

@app.get("/")
def home_page():
    return {"Hi Anshika, Welcome to the first step of your success"}

@app.get("/courses")
def get_all_courses():
    return fakedb

@app.get("/courses/{course_id}")
def get_course_by_id(course_id: int):
    course  = course_id - 1
    return fakedb[course]


@app.post("/courses")
def add_course(course: Course):
    fakedb.append(course.dict())
    return fakedb[-1]

@app.delete("/course/{course_id}")
def delete_by_id(course_id: int):
    fakedb.pop(course_id-1)
    return {
        "msg": "deleted successfully",
        "status": "200OK"}