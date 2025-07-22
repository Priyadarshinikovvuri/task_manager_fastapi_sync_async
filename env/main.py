from fastapi import FastAPI
import task_sync
import task_async

app = FastAPI(title="Simple Task Manager (Sync & Async)")

# Add both routers
app.include_router(task_sync.router, prefix="/sync", tags=["Sync Tasks"])
app.include_router(task_async.router, prefix="/async", tags=["Async Tasks"])
