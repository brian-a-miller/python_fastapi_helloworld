from fastapi import FastAPI
from sqlmodel import SQLModel

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
