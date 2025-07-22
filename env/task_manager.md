
# Task Manager using FastAPI - CRUD Operation (Sync & Async with In-Memory Data)

This guide helps you build a simple **Task Manager API** using FastAPI with:

- Only Python list as storage (no database)
- Two main APIs: `Create` and `Get All`
- Both **synchronous** and **asynchronous** versions

---

## 1. Setup Instructions

### Step 1: Create Project Folder

```bash
mkdir fastapi_task_manager
cd fastapi_task_manager
```

### Step 2: Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### Step 3: Install FastAPI & Uvicorn

```bash
pip install fastapi uvicorn
```

---

## 2. Project Structure

```
fastapi_task_manager/
├── main.py
├── task_sync.py
└── task_async.py
```

---

## 3. Create a Simple Task Model

We will use this structure:

```python
# A task looks like this:
{
    "id": 1,
    "title": "Learn FastAPI",
    "done": False
}
```

---

## 4. Synchronous API - `task_sync.py`

```python
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

tasks = []
task_id_counter = 1

class Task(BaseModel):
    title: str
    done: bool = False

@router.post("/create")
def create_task(task: Task):
    global task_id_counter
    new_task = {"id": task_id_counter, "title": task.title, "done": task.done}
    tasks.append(new_task)
    task_id_counter += 1
    return {"message": "Task created", "task": new_task}

@router.get("/all")
def get_tasks():
    return {"tasks": tasks}
```

---

## 5. Asynchronous API - `task_async.py`

```python
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

tasks_async = []
task_id_async = 1

class Task(BaseModel):
    title: str
    done: bool = False

@router.post("/create")
async def create_task_async(task: Task):
    global task_id_async
    new_task = {"id": task_id_async, "title": task.title, "done": task.done}
    tasks_async.append(new_task)
    task_id_async += 1
    return {"message": "Task created (async)", "task": new_task}

@router.get("/all")
async def get_tasks_async():
    return {"tasks": tasks_async}
```

---

## 6. Main FastAPI App - `main.py`

```python
from fastapi import FastAPI
import task_sync
import task_async

app = FastAPI(title="Simple Task Manager (Sync & Async)")

app.include_router(task_sync.router, prefix="/sync", tags=["Synchronous Tasks"])
app.include_router(task_async.router, prefix="/async", tags=["Asynchronous Tasks"])
```

---

## 7. Run the App

```bash
uvicorn main:app --reload
```

Open your browser at:

- [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Interview Questions Based on This Project

### FastAPI & Project Design
1. What is FastAPI and why did you choose it for this project?
2. What are the advantages of FastAPI compared to Flask or Django?
3. What is the role of `main.py` in your FastAPI project?
4. How do you organize your project structure and why?
5. What is the purpose of `@app.get()` and `@app.post()` decorators?

### CRUD Operations
6. What are CRUD operations? How did you implement them?
7. How many endpoints have you implemented and what does each do?
8. Can you explain how your task creation and retrieval APIs work?

### Sync vs Async
9. What is the difference between sync and async functions in FastAPI?
10. In which file did you use `async def`, and why?
11. When would you prefer using `async` over `sync` in FastAPI?

### Implementation & Environment
12. What is a virtual environment and why did you use it?
13. What packages did you install to run this project?
14. What is the use of `requirements.txt`?
15. How do you run this FastAPI application locally?

---

