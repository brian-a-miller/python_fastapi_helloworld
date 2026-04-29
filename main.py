from fastapi import FastAPI
from sqlmodel import SQLModel
from datetime import datetime

# --- The App ---
app = FastAPI(title="Hello API", version="1.0.0")

# --- A SQLModel (Pydantic + SQLAlchemy combined) ---
class Greeting(SQLModel):
    name: str
    message: str

# --- A simple GET endpoint ---
@app.get("/")
def root():
    return {"message": "Hello, World!"}

# --- A GET endpoint with a path parameter ---
@app.get("/hello/{name}", response_model=Greeting)
def say_hello(name: str):
    return Greeting(name=name, message=f"Hello, {name}! Welcome to the API.")

# --- A simple GET endpoint which returns today's date ---
@app.get("/todaysdate")
def get_date():
    now = datetime.now()
    iso = now.date().isoformat()
    return {
        "month": now.month,
        "day": now.day,
        "year": now.year,
        "full_date": now.strftime("%B %d, %Y"),
        "isoformat": iso,
    }
