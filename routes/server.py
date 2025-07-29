from fastapi import APIRouter

router = APIRouter(prefix="/server", tags=["server"])

import platform
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

@router.get("/info")
def get_server_info():
    return {
        "server": "FastAPI Example",
        "status": "running",
        "os": platform.system(),
        "os_version": platform.version(),
        "platform": platform.platform(),
        "python_version": platform.python_version(),
        "hostname": platform.node(),
        "cwd": os.getcwd(),
        "timestamp": datetime.now().isoformat(),
        "project_version": os.getenv("PROJECT_VERSION", "unknown")
    }
