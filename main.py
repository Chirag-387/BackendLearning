from fastapi import FastAPI, HTTPException, status

app = FastAPI()


data: list[dict] = [
    {
        "id": 1,
        "name": "random1",
        "skill": "web_dev",
    },
    {
        "id": 2,
        "name": "random2",
        "skill": "app_dev",
    },
]


@app.get("/")
def home():
    return {
        "message": "Hello, World!"
    }

@app.get("/api/data")
def get_datas():
    return data

@app.get("/api/data/{data_id}")
def get_data(data_id: int):
    for val in data:
        if val["id"] == data_id:
            return val
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Post not found")