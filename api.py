from fastapi import FastAPI, HTTPException
import json, os

app = FastAPI(title="fasion design Colleges API")

DATA_FILE = "top_fasion_design_college_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

@app.get("/")
async def root():
    return {"message": "API is running! Go to /fasion_design_colleges to see all colleges."}

@app.get("/medical_design")
async def get_all_colleges():
    return {"/medical_design": load_data()}

@app.get("/medical_design/{college_id}")
async def get_college_by_id(college_id: int):
    data = load_data()
    idx = 1
    for section in data:
        for college in section["colleges"]:
            if idx == college_id:
                return college
            idx += 1
    raise HTTPException(status_code=404, detail="College not found")
