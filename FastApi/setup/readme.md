# <div align='center'> 🔰 FastApi Setup </div>

## 📌 Table of Contents

## 👉 Create Virtual Environment
```bash
python -m venv ./venv-fastapi
```

- This will create a virtual environment in the current directory.
- It will also create a folder called `venv-fastapi` which will contain all the necessary packages for our FastApi project.

## 👉 Activate the Virtual Environment
```bash
. venv-fastapi/Scripts/activate
```

- This will activate the virtual environment.
- This means that any packages we install will be installed in the `venv-fastapi` folder.
- This is useful because it allows us to keep our project dependencies separate from the global dependencies.

## 👉 Install FastApi
```bash
pip install fastapi
```

- This will install FastApi in the virtual environment.
- FastApi is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

## 👉 Install Uvicorn
```bash
pip install "uvicorn[standard]"
```

- This will install Uvicorn in the virtual environment.
- Uvicorn is a lightning-fast ASGI server implementation, using uvloop and httptools. (ASGI is a standard for Python asynchronous web apps and servers to communicate with each other.)

## 👉 Create `main.py` file and run code
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index():
    return {"message": "Hello, World!"}
```

- This will create a simple FastApi app that returns a JSON response with the message "Hello, World!".
- `main.py` is the entry point of our FastApi app.
- To run the app, use the following command:
```bash
uvicorn main:app --reload
```

- This will start the Uvicorn server and run the FastApi app.
- The `--reload` flag is used to automatically reload the server when changes are made to the code.
- We can access the app at `http://localhost:8000/`.