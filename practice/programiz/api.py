from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get("/")
def start():
    return {'message': 'hello'}

@app.get("/hello")
def hello():
    return{'message': 'patient api system'}


if __name__ == "__main__":
    uvicorn.run("api:app", host = "0.0.0.0", port = 5555, reload = True)