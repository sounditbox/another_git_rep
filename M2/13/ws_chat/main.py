import asyncio
import json

from websockets.asyncio.server import broadcast, Connection, serve

users = set()
messages = []


# {'type': 'message', 'message': 'Hello!'}
# {'type': 'join', 'users_count': n}


def join_json() -> str:
    return json.dumps({"type": "join", 'users_count': len(users)})


def message_json(message) -> str:
    return json.dumps({"type": "message", "message": message})


def leave_json() -> str:
    return json.dumps({"type": "leave", 'users_count': len(users)})


def update_json() -> str:
    return json.dumps({"type": "update", "messages": messages})


async def handler(connection: Connection):
    try:
        users.add(connection)
        async for message in connection:
            data = json.loads(message)
            if data["type"] == "join":
                broadcast(users, join_json())
                await connection.send(update_json())
            elif data["type"] == "message":
                messages.append(data["message"])
                broadcast(users, message_json(data["message"]))
            else:
                await connection.close(1003, "Unsupported message type")

    finally:
        broadcast(users, leave_json())
        users.remove(connection)


async def main():
    async with serve(handler, "localhost", 80):
        await asyncio.get_running_loop().create_future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
