from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

jobs = {}

class JobRequest(BaseModel):
    title: str

@app.post("/jobs")
def create_job():
    job_id = len(jobs) + 1
    jobs[job_id] = "created"
    return {"job_id": job_id, "status": "created"}