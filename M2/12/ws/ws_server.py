#!/usr/bin/env python

"""Echo server using the asyncio API."""

import asyncio

from websockets.asyncio.server import serve


async def message_handler(websocket):
    async for message in websocket:
        print(f"Received from client: {message}")
        answer = input("Your answer:\n")

        await websocket.send(answer)


async def main():
    async with serve(message_handler, "localhost", 8765) as server:
        print('WebSocket server started on ws://localhost:8765')
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
