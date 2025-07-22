from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

# In-memory async task list
tasks_async = []
task_id_async = 1

# Pydantic model for request
class Task(BaseModel):
    title: str
    done: bool = False

# Async Create Task (POST)
@router.post("/create")
async def create_task_async(task: Task):
    global task_id_async
    new_task = {"id": task_id_async, "title": task.title, "done": task.done}
    tasks_async.append(new_task)
    task_id_async += 1
    return {"message": "Task created (async)", "task": new_task}

# Async Get All Tasks (GET)
@router.get("/all")
async def get_tasks_async():
    return {"tasks": tasks_async}
