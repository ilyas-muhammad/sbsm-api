from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from model import Measurement
from spreadsheet import append_row, get_all_records

app = FastAPI()

load_dotenv()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def ping():
    return {"message": "Hello, Python!"}

@app.post("/measurement-sync")
async def measurement_sync(measurement: Measurement):
    try:
        append_row(measurement)
        return {"message": "Measurement synced successfully", "data": measurement}
    except Exception as e:
        print(e)
        return {"message": "Measurement sync failed", "error": str(e)}, 500

@app.get("/measurement-sync/all")
async def measurement_sync_all():
    return {"message": "Measurement synced successfully", "data": get_all_records()}