#  start1
from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def home():
    return {"siva sasdhfo"}

@app.get("/about")
def about():
    return {"siva is great"}
