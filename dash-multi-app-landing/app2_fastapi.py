from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from datetime import datetime
from typing import List, Optional
import os

app = FastAPI(title="Chat Application 2", description="FastAPI-based chat app with green theme")

# Mount static files
if not os.path.exists("static"):
    os.makedirs("static")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup templates
if not os.path.exists("templates"):
    os.makedirs("templates")
templates = Jinja2Templates(directory="templates")

# In-memory storage for messages
messages: List[dict] = []

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("app2.html", {"request": request, "messages": messages})

@app.post("/send")
async def send_message(message: str = Form(...)):
    if message.strip():
        new_message = {
            "text": message,
            "timestamp": datetime.now().strftime("%H:%M:%S"),
            "id": len(messages) + 1
        }
        messages.append(new_message)
    return {"success": True, "message_count": len(messages)}

@app.get("/messages")
async def get_messages():
    return {"messages": messages}

@app.delete("/clear")
async def clear_messages():
    global messages
    messages = []
    return {"success": True, "message": "Chat cleared"}

if __name__ == "__main__":
    uvicorn.run("app2_fastapi:app", host="127.0.0.1", port=8052, reload=True)
