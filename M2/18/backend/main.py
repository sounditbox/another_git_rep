import os

from dotenv import load_dotenv
from fastapi import FastAPI, WebSocket, HTTPException
from loguru import logger
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator
from gpt import ChatGptService

from prometheus_client import Counter

app = FastAPI()
Instrumentator().instrument(app).expose(app)
logger.add("./logs/app.log", format="{time} - {level} - {message}",
           level='DEBUG')
load_dotenv()
TOKEN = os.getenv("OPENAI_API_KEY")
gpt = ChatGptService(TOKEN)
gpt.set_prompt('Ты - самый лучший и полезный ассистент в мире!')

METRIC = Counter(
    "http_requested_versions_changed",
    "Number of times any version LLM was set.",
    labelnames=("vers",)
)
origins = [
    '*'
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            logger.info(f'User sends: {data}')
            answer = await gpt.add_message(data)
            logger.info(f'Answer: {answer}')
            await websocket.send_text(answer)
    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        await websocket.close()


@app.get("/")
async def main():
    return {"message": "Hello World"}


@app.get("/versions")
async def get_versions():
    return {
        'versions': ["gpt-3.5-turbo",
                     'gpt-4o', 'gpt-4-turbo', 'gpt-3.5-turbo',
                     'GPT-4o mini']
    }


class VersionRequest(BaseModel):
    version: str


@app.post("/set_version")
async def set_version(version_request: VersionRequest):
    global selected_version
    if version_request.version not in ["gpt-3.5-turbo", "gpt-4o", "gpt-4-turbo",
                                       "GPT-4o mini"]:
        raise HTTPException(status_code=400, detail="Неверная версия модели")

    selected_version = version_request.version
    return {"message": f"Версия успешно изменена на {selected_version}"}


@app.get("/versions")
async def get_versions():
    logger.info('Getting versions')
    return {
        'versions': ["gpt-3.5-turbo", "gpt-4o", "gpt-4-turbo", "GPT-4o mini"]
    }


@app.get("/metrics")
async def get_metrics():
    logger.info('Getting metrics')
    return {'metrics': 'metrics'}


