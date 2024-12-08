# client.py
import asyncio
import websockets

async def send_message():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        message = "Mateo Carrasco Progra Distribuida"
        print(f"Enviando mensaje: {message}")
        await websocket.send(message)
        response = await websocket.recv()
        print(f"Respuesta del servidor: {response}")

if __name__ == "__main__":
    asyncio.run(send_message())
