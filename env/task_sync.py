from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

# In-memory storage
tasks = []
task_id = 1  # Start with ID 1

# Pydantic model for incoming task data
class Task(BaseModel):
    title: str
    done: bool = False

# Create Task (POST)
@router.post("/create")
def create_task(task: Task):
    global task_id
    new_task = {"id": task_id, "title": task.title, "done": task.done}
    tasks.append(new_task)
    task_id += 1
    return {"message": "Task created", "task": new_task}

# Get All Tasks (GET)
@router.get("/all")
def get_all_tasks():
    return {"tasks": tasks}
