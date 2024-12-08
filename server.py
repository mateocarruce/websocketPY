import asyncio
import websockets

async def hello(websocket):
    print("Cliente conectado")
    async for message in websocket:
        print(f"Mensaje recibido: {message}")
        await websocket.send(f"Hola {message}")

async def main():
    async with websockets.serve(hello, "0.0.0.0", 8765):
        print("Servidor corriendo en ws://0.0.0.0:8765")
        await asyncio.Future()  # Ejecutar indefinidamente

if __name__ == "__main__":
    asyncio.run(main())
