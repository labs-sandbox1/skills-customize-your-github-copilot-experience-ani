# Starter code for FastAPI REST API assignment

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to your FastAPI API!"}

# Add CRUD endpoints below

# Example data structure
items = []

# Example: Add more endpoints for Create, Read, Update, Delete

# Example: Add test cases in a separate file or section
