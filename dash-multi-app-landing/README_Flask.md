# Flask Multi-App Dashboard

A Flask-based web application that serves as a launcher for multiple Dash applications.

## Features

- Modern, responsive web interface using Bootstrap 5
- Red-themed design with hover effects and animations
- AJAX-based app launching with real-time feedback
- Toast notifications for success/error messages
- Automatic browser tab opening for launched apps

## Project Structure

```
├── flask_app.py          # Main Flask application
├── templates/
│   └── index.html        # Main dashboard template
├── static/
│   ├── style.css         # Custom CSS styles
│   └── script.js         # JavaScript for interactions
├── apps_config.toml      # Configuration for available apps
├── app1.py              # Sample Dash app 1
├── app2.py              # Sample Dash app 2
└── requirements.txt     # Python dependencies
```

## Installation

1. Make sure you have Python installed
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask dashboard:
   ```bash
   python flask_app.py
   ```

2. Open your browser and navigate to:
   ```
   http://localhost:8080
   ```

3. Click on any "Launch Application" button to start the corresponding Dash app

## Configuration

Edit `apps_config.toml` to add or modify applications:

```toml
[app_name]
filename = "app_file.py"
name = "Display Name"
port = 8051
description = "App description"
color = "primary"
```

## Features Comparison: Dash vs Flask

### Original Dash Version
- Uses Dash components and callbacks
- Reactive programming model
- Built-in Bootstrap components

### New Flask Version
- Traditional Flask routes and templates
- HTML templates with Jinja2
- Custom CSS and JavaScript
- AJAX for dynamic interactions
- Toast notifications
- Better error handling
- More flexible styling options

## Browser Compatibility

- Chrome/Edge (recommended)
- Firefox
- Safari
- Modern mobile browsers

The application will automatically open new browser tabs for launched apps and provide visual feedback during the launch process.
