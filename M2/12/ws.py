import asyncio

import websockets

host, port = "localhost", 8765


async def echo_handler(websocket, path):
    await websocket.send("Hello! You are connected to the WebSocket server.")
    async for message in websocket:
        print(f"Received from client: {message}")
        await websocket.send(f"Server Echo: {message}")


async def main():
    async with websockets.serve(echo_handler, host, port):
        print(f"WebSocket server started on ws://{host}:{port}")
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
