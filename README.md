# Rhythm-of-Pi

## Overview

Rhythm-of-Pi is a music generation platform that leverages the Suno API to generate audio files from text prompts. It stores and manages user information, song data, and difficulty levels using a PostgreSQL database.

## Project Structure

```
Rhythm-of-Pi/
├── .venv/                  # Virtual environment
├── database/               # Database-related files
│   ├── __init__.py         # Initializes database module
│   ├── database.py         # Database connection and session handling
│   ├── error_handler.py    # Error handler for database operations
│   └── models.py           # SQLAlchemy ORM models for User, Song, and Level
├── endpoints/              # API endpoints
│   ├── __init__.py         # Initializes API endpoints
│   ├── api.py              # Main API router
│   ├── deps.py             # Dependency injection and database instance
│   ├── generation.py       # Audio generation endpoints
│   ├── levels.py           # Level retrieval endpoints
│   └── registration.py     # User registration and management
├── modules/                # Additional modules
│   ├── __init__.py         # Initializes modules
│   ├── generate_pi.py      # Generates and saves chunks of Pi digits
│   └── suno_api.py         # Suno API client for audio generation
├── .env                    # Environment variables
├── .gitignore              # Files and directories to ignore in git
├── config.ini              # Configuration file for Suno API and other settings
├── main.py                 # Entry point for FastAPI application
├── Procfile                # Deployment configuration for Heroku
└── requirements.txt        # Project dependencies
```

## File Descriptions

### database/
- `__init__.py`: Initializes the database package.
- `database.py`: Establishes connection to PostgreSQL and handles session creation.
- `error_handler.py`: Handles errors related to database transactions.
- `models.py`: Defines ORM models for User, Song, and Level tables.

### endpoints/
- `__init__.py`: Initializes the API endpoints package.
- `api.py`: Main router that includes different endpoints.
- `deps.py`: Dependency management for database interactions.
- `generation.py`: Handles audio generation requests and callbacks.
- `levels.py`: Retrieves difficulty levels.
- `registration.py`: Manages user registration and IP tracking.

### modules/
- `__init__.py`: Initializes the modules package.
- `generate_pi.py`: Generates Pi digits in chunks and saves them to JSON.
- `suno_api.py`: Manages Suno API interactions, task creation, and audio download.

## Installation

### Prerequisites
- Python 3.9+
- PostgreSQL
- Virtual Environment (recommended)

### Steps
```bash
# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate   # On Linux/Mac
# or
.venv\Scripts\activate     # On Windows

# Install dependencies
pip install -r requirements.txt
```

### Environment Variables
Set up your `.env` file with the following variables:
```
SUNO_API_TOKEN=<your-suno-api-token>
DOMAIN=<your-domain>
DB_HOST=<your-db-host>
DB_PORT=<your-db-port>
DB_USERNAME=<your-db-username>
DB_PASSWORD=<your-db-password>
DB_DATABASE=<your-db-name>
DB_SSLMODE=require
```

## Usage

### Run the application
```bash
# Run the FastAPI server
uvicorn main:app --host 0.0.0.0 --port 8000
```

### API Endpoints

- `POST /api/registration/add_user/{ip}/{hash}` - Add a new user
- `POST /api/generation/generate_audio/{prompt}/{hash}` - Generate audio
- `POST /api/generation/callback/{hash}` - Handle Suno API callback
- `GET /api/levels/get_levels` - Retrieve difficulty levels
- `GET /api/generation/get_audio/{hash}/{task_id}` - Get generated audio

## Deployment

### Heroku
```bash
# Login to Heroku
heroku login

# Create Heroku app
heroku create rhythm-of-pi

# Push to Heroku
git push heroku main

# Set environment variables
heroku config:set $(cat .env | xargs)

# Scale dynos
heroku ps:scale web=1
```
