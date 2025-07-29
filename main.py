from fastapi import FastAPI
from routes.server import router as server_router
from routes.users import router as users_router
from routes.posts import router as posts_router

app = FastAPI()

# Root endpoint for compatibility
default_root_message = {"message": "Hello, World!"}

@app.get("/")
def read_root():
    return default_root_message

# Include modular routers
app.include_router(server_router)
app.include_router(users_router)
app.include_router(posts_router)
