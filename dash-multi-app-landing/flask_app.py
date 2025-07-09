from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
import toml
import subprocess
import sys
import os
import webbrowser
import time
from threading import Timer
import uvicorn

app = FastAPI(title="Multi-App Dashboard", description="FastAPI-based multi-app launcher")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup templates
templates = Jinja2Templates(directory="templates")

# Load configuration
with open('apps_config.toml', 'r') as f:
    config = toml.load(f)

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "apps": config})

@app.get("/launch/{app_key}")
async def launch_app(app_key: str):
    if app_key not in config:
        raise HTTPException(status_code=404, detail="App not found")
    
    app_info = config[app_key]
    filename = app_info['filename']
    port = app_info['port']
    
    try:
        # Start the FastAPI app process
        process = subprocess.Popen(
            [sys.executable, filename],
            cwd=os.path.dirname(os.path.abspath(__file__)),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Wait a moment for the app to start
        time.sleep(3)
        
        # Open the browser to the app URL
        url = f"http://localhost:{port}"
        Timer(0.1, lambda: webbrowser.open_new_tab(url)).start()
        
        return {"success": True, "message": "App launched successfully", "url": url}
    except Exception as e:
        return {"success": False, "message": f"Error launching app: {str(e)}"}

if __name__ == '__main__':
    uvicorn.run("flask_app:app", host="127.0.0.1", port=8080, reload=True)
