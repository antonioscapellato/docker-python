# FastAPI + Docker Example

This project is a minimal Python backend using [FastAPI](https://fastapi.tiangolo.com/) that can be run both locally and inside a Docker container. It provides a simple API endpoint and is ready for extension.

## Features
- FastAPI backend with a single root endpoint (`GET /`)
- Dockerfile for easy containerization
- `requirements.txt` for dependency management

## Project Structure
```
.
├── main.py            # FastAPI application
├── requirements.txt   # Python dependencies
├── Dockerfile         # Docker container instructions
└── README.md          # Project overview and instructions
```

## Getting Started

### 1. Run Locally (without Docker)

1. **Install dependencies** (preferably in a virtual environment):
    ```bash
    pip install -r requirements.txt
    ```
2. **Start the server:**
    ```bash
    python -m uvicorn main:app --host 127.0.0.1 --port 8000
    ```
3. **Access the API:**
    - Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.
    - Interactive docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### 2. Run with Docker

1. **Build the Docker image:**
    ```bash
    docker build -t docker-python .
    ```
2. **Run the Docker container:**
    ```bash
    docker run -p 8000:8000 docker-python
    ```
3. **Access the API:**
    - Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.
    - Interactive docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Example Endpoint
- `GET /` — returns `{ "message": "Hello, World!" }`

## Extending the App
You can add more endpoints to `main.py` using FastAPI's syntax. See the [FastAPI documentation](https://fastapi.tiangolo.com/tutorial/) for more details.

---

Feel free to use this as a template for your own projects!
