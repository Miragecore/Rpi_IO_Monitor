import os
import sys
import logging
import uvicorn
import asyncio
import json
#import gpiozero
from gpiozero import Button

from enum import Enum
from fastapi import FastAPI, Request, APIRouter
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi import WebSocket

from fastapi.logger import logger

from os.path import exists

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

logging.info("load machine info")

machineInfofile = './machineInfo.json'

file_exists = exists(machineInfofile)
if not file_exists :
    logging.error("Cann't found machineInfo.json");
    exit()

machine_info = {}

with open(machineInfofile) as mInfojson:
    machine_info = json.load(mInfojson);

logging.info(machine_info)

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
logging.info("BASE_DIR :" + BASE_DIR)

templates = Jinja2Templates(directory="static")

FRONT_END_PATH = "static/public"
logging.info("FRONT_END_PATH : " + FRONT_END_PATH)

def machine_IO_On():
    logging.info("IO On")
    machine_info["0"]["status"] = 1

def machine_IO_Off():
    logging.info("IO Off")
    machine_info["0"]["status"] = 0

#button = Button(21)

#button.when_pressed = machine_IO_on
#button.when_released = machine_IO_Off

app = FastAPI()

origins = [
    "http://localhost:8000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/public", StaticFiles(directory=os.path.join(BASE_DIR, FRONT_END_PATH)), name="public")

api_router = APIRouter()

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", context={"request": request})

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        await asyncio.sleep(3)
        await websocket.send_json(machine_info)

app.include_router(api_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
