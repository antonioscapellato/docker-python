# FastAPI + Docker Template Example

This project is a minimal Python backend using [FastAPI](https://fastapi.tiangolo.com/) that can be run both locally and inside a Docker container. It provides a simple API endpoint and is ready for extension.

## Features
- FastAPI backend with a single root endpoint (`GET /`)
- Dockerfile for easy containerization
- `requirements.txt` for dependency management

## Project Structure
```
.
├── main.py              # FastAPI application entrypoint
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker container instructions
├── .gitignore           # Git ignore rules
├── .env                 # Environment variables
├── README.md            # Project overview and instructions
└── routes/              # All API route modules
    ├── server.py        # /server/info endpoint
    ├── users.py         # /users endpoints
    └── posts.py         # /posts endpoints
```

## Getting Started

### 1. Run Locally (without Docker)

1. **Configure environment variables:**
    - Edit the `.env` file to set project variables (e.g., `PROJECT_VERSION=0.0.1`).
2. **Install dependencies** (preferably in a virtual environment):
    ```bash
    pip install -r requirements.txt
    ```
3. **Start the server:**
    ```bash
    python -m uvicorn main:app --host 127.0.0.1 --port 8000
    ```
4. **Access the API:**
    - Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.
    - Interactive docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### 2. Run with Docker

1. **Configure environment variables:**
    - Edit the `.env` file before building the image. Docker will copy this file into the container.
2. **Build the Docker image:**
    ```bash
    docker build -t docker-python .
    ```
3. **Run the Docker container:**
    ```bash
    docker run -p 8000:8000 docker-python
    ```
4. **Access the API:**
    - Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.
    - Interactive docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Example Endpoints
- `GET /` — returns `{ "message": "Hello, World!" }`
- `GET /server/info` — returns server stats, OS info, timestamp, and `PROJECT_VERSION` from environment variables
- `GET /users/get` — get all users (in-memory example)
- `POST /users/add` — add a user (in-memory example)
- `GET /posts/get` — get all posts (in-memory example)
- `POST /posts/add` — add a post (in-memory example)

## Environment Variables
- Edit the `.env` file to set project-specific variables.
- Example:
    ```env
    PROJECT_VERSION=0.0.1
    ```
- These will be available in your code via `os.getenv()` and shown in `/server/info`.

## Extending the App
- Add new endpoints by creating new files in the `routes/` folder and including their routers in `main.py`.
- See the [FastAPI documentation](https://fastapi.tiangolo.com/tutorial/) for more details.

---

Feel free to use this as a template for your own projects! 

By [Antonio Scapellato](https://scapellato.dev)
