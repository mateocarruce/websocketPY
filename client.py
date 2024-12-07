# client.py
import asyncio
import websockets

async def send_message():
    async with websockets.connect("ws://localhost:8765") as websocket:
        message = "Mateo Carrasco"
        await websocket.send(message)
        print(f"Sent message: {message}")

        response = await websocket.recv()
        print(f"Received message: {response}")

asyncio.run(send_message())
