from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse

app = FastAPI()

# Página HTML simple para interactuar con el WebSocket
html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>WebSocket Chat</title>
</head>
<body>
    <h1>WebSocket Chat</h1>
    <textarea id="messages" cols="100" rows="20" readonly></textarea><br><br>
    <input type="text" id="message" placeholder="Type a message" />
    <button onclick="sendMessage()">Send</button>

    <script>
        var ws = new WebSocket("ws://localhost:8000/ws/chat/");
        ws.onmessage = function(event) {
            document.getElementById("messages").value += event.data + '\\n';
        };

        function sendMessage() {
            var message = document.getElementById("message").value;
            ws.send(message);
            document.getElementById("message").value = "";
        }
    </script>
</body>
</html>
"""

@app.get("/")
async def get():
    return HTMLResponse(content=html)

# WebSocket endpoint
@app.websocket("/ws/chat/")
async def chat_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message received: {data}")
    except WebSocketDisconnect:
        print("Client disconnected")
