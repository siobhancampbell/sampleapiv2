from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return 'Hello World!'


@app.get("/persons")
def read_item():
    persons = ['Person 1', 'Person 2', 'Person 3']
    return persons

if __name__ == '__main__':
    uvicorn.run(app, port=80, host="0.0.0.0")
    uvicorn.run(app)