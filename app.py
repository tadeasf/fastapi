try:
    import unzip_requirements
except ImportError:
    pass
from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()


@app.get("/v1/api")
def hello_world():
    return {"message": "Hello from FastAPI"}


@app.get("/v1/api/hello/{name}")
def hello(name: str):
    return {"message": f"Hello from FastAPI, {name}!"}

handler = Mangum(app)
