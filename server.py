from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import jsonDataHandler as data

app = FastAPI()

@app.get("/")
async def get_index():
    return None

@app.get("/read/")
async def read_file_by_name(name: str):
    return data.read_json(name)

@app.get("/read-all/", "Breaking change")
async def read_all():
    return data.read_all()

@app.get("/read-range/")
async def read_in_range(start_date: str="2025-03-13", end_date: str="2025-03-13"):
    return data.filter_date_range(start_date, end_date)