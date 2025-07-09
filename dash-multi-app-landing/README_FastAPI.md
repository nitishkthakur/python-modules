# FastAPI Multi-App Dashboard

A FastAPI-based web application that serves as a launcher for multiple FastAPI chat applications.

## Features

- **Modern FastAPI Architecture**: Async/await support, automatic API documentation
- **Responsive Web Interface**: Bootstrap 5 with custom red theme
- **Real-time Chat Applications**: Two separate chat apps with different themes
- **AJAX Interactions**: Dynamic app launching with feedback
- **Toast Notifications**: Success/error messages
- **Auto-documentation**: FastAPI automatically generates API docs at `/docs`

## Project Structure

```
├── fastapi_app.py        # Main FastAPI launcher application
├── app1_fastapi.py       # Chat app 1 (blue theme)
├── app2_fastapi.py       # Chat app 2 (green theme)
├── templates/
│   ├── index.html        # Main dashboard template
│   ├── app1.html         # Chat app 1 template
│   └── app2.html         # Chat app 2 template
├── static/
│   ├── style.css         # Custom CSS styles
│   └── script.js         # JavaScript for interactions
├── apps_config.toml      # Configuration for available apps
└── requirements.txt      # Python dependencies
```

## Installation

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Starting the Main Dashboard

1. Start the FastAPI dashboard:
   ```bash
   python fastapi_app.py
   ```

2. Open your browser and navigate to:
   ```
   http://localhost:8080
   ```

3. View the auto-generated API documentation:
   ```
   http://localhost:8080/docs
   ```

### Starting Individual Apps

You can also run the chat applications directly:

```bash
# Chat App 1 (Blue theme)
python app1_fastapi.py
# Access at http://localhost:8051

# Chat App 2 (Green theme)  
python app2_fastapi.py
# Access at http://localhost:8052
```

## API Endpoints

### Main Dashboard (Port 8080)
- `GET /` - Main dashboard page
- `GET /launch/{app_key}` - Launch a specific app

### Chat Applications (Ports 8051, 8052)
- `GET /` - Chat interface
- `POST /send` - Send a message
- `GET /messages` - Get all messages
- `DELETE /clear` - Clear all messages

## Features Comparison: Dash → Flask → FastAPI

### FastAPI Advantages
- **Performance**: Much faster than Flask/Dash due to async support
- **Type Safety**: Built-in type hints and validation
- **Auto Documentation**: Automatic OpenAPI/Swagger docs
- **Modern Python**: Async/await, Python 3.7+ features
- **API-First**: Designed for building APIs and web services
- **WebSocket Support**: Built-in support for real-time features
- **Dependency Injection**: Advanced dependency injection system

### Architecture Benefits
- **Separation of Concerns**: Clear separation between API and UI
- **Scalability**: Better performance under load
- **Testing**: Better testing support with pytest integration
- **Development**: Hot reload and better error messages
- **Production Ready**: Built-in support for production deployment

## Configuration

Edit `apps_config.toml` to add or modify applications:

```toml
[app_name]
filename = "app_file_fastapi.py"
name = "Display Name"
port = 8051
description = "App description"
color = "primary"
```

## Chat Application Features

Both chat applications include:
- **Real-time Messaging**: Send and receive messages
- **Message Persistence**: Messages stored in memory during session
- **Auto-refresh**: Messages update every 2 seconds
- **Clear Chat**: Button to clear all messages
- **Timestamps**: Each message shows the time sent
- **Responsive Design**: Works on desktop and mobile

## Development

### Running in Development Mode
All FastAPI apps include hot reload by default when run with `python app_name.py`.

### API Documentation
Each FastAPI app automatically generates API documentation:
- Main app: http://localhost:8080/docs
- Chat app 1: http://localhost:8051/docs  
- Chat app 2: http://localhost:8052/docs

### Production Deployment
For production, use uvicorn directly:
```bash
uvicorn fastapi_app:app --host 0.0.0.0 --port 8080
```

## Browser Compatibility
- Chrome/Edge (recommended)
- Firefox
- Safari
- Modern mobile browsers

The FastAPI version provides significant performance improvements and modern Python features while maintaining the same user experience as the previous Flask/Dash versions.
