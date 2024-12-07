# server.py
import asyncio
import websockets

async def hello(websocket, path):
    name = await websocket.recv()
    print(f"Received message: {name}")

    response = f"Hello {name}!"
    await websocket.send(response)
    print(f"Sent message: {response}")

start_server = websockets.serve(hello, "0.0.0.0", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
