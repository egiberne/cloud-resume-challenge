from fastapi import FastAPI

app = FastAPI()

## GET REQUESTS
@app.get("/")
def read_root():
    return {"Hello": "World"}



@app.get("/api/hello")
def hello(name: str = "World"):
    return { f"Hello, {name}!"}

from pydantic import BaseModel
class HelloRequest(BaseModel):
 name: str

@app.post("/api/helloUser") 
def hello(request: HelloRequest):
    return {f"Hello, {request.name}!"}