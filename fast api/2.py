from fastapi import FastAPI
from pydantic import BaseModel


class Student(BaseModel):
    id: int
    name: str


app = FastAPI()

students =[
    {"id":1,"name":"siva"},
    {"id": 2, "name":"Shankar"}
]

@app.get("/student")
def get_students():
    return students


