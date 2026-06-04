# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to design and build a simple REST API using FastAPI. This assignment covers defining routes, request validation, response models, and running a FastAPI application.

## 📝 Tasks

### 🛠️ Create API endpoints

#### Description
Build a FastAPI application with endpoints for managing a sample resource such as books, tasks, or notes.

#### Requirements
Completed program should:

- Define a FastAPI app in `main.py`
- Create at least two routes: one `GET` endpoint and one `POST` endpoint
- Use Pydantic models to validate request data
- Return JSON responses with appropriate status codes
- Include clear route names and descriptions

### 🛠️ Add validation and documentation

#### Description
Use FastAPI features to validate incoming data and make the API self-documenting.

#### Requirements
Completed program should:

- Define request and response models using Pydantic
- Validate required fields and data types automatically
- Return a meaningful error message for invalid input
- Expose interactive API docs at `/docs`
- Include example data or sample usage in comments if helpful
