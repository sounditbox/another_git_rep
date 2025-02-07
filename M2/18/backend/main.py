import os

from dotenv import load_dotenv
from fastapi import FastAPI, WebSocket, HTTPException
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

from gpt import ChatGptService

app = FastAPI()
load_dotenv()
TOKEN = os.getenv("OPENAI_API_KEY")
gpt = ChatGptService(TOKEN)
gpt.set_prompt('Ты - самый лучший и полезный ассистент в мире!')


origins = [
    "http://localhost",
    "http://localhost:80",
    "http://127.0.0.1",
    "http://127.0.0.1:3000"
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
            answer = await gpt.add_message(data)
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
    return {
        'versions': ["gpt-3.5-turbo", "gpt-4o", "gpt-4-turbo", "GPT-4o mini"]
    }
