A full-stack AI-powered Weather Assistant built using React (frontend) and FastAPI (backend). The application fetches real-time weather data using OpenWeather API and generates natural language responses using LangChain + OpenRouter LLM.

**Features**
React-based frontend UI
FastAPI backend
Real-time weather data (OpenWeather API)
AI-generated responses using OpenRouter LLM
Clean separation of frontend and backend
Simple setup and execution

**Tech Stack**
**Frontend**
React
JavaScript
Fetch API
**Backend**
Python
FastAPI
LangChain
OpenRouter
OpenWeather API

**Project Structure**
sanchai-weather-app/
│
├── backend/
│   ├── main.py
│   ├── agent.py
│   ├── tools.py
│   ├── .env        # (not committed, user must create)
│   └── .gitignore
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   ├── .gitignore
│
└── README.md

**Prerequisites**
Make sure you have the following installed:
Node.js (v16 or above)
Python (v3.10+ recommended)
pip
Git

**Environment Variables Setup**
Backend .env file
Create a file named **.env** inside the backend/ folder.
env
OPENROUTER_API_KEY=your_openrouter_api_key_here
OPENWEATHER_API_KEY=your_openweather_api_key_here

**Backend setup**
cd backend ->
python -m venv venv(optional but recommended) ->
venv\Scripts\activate(Windows)/ source venv/bin/activate(Mac/Linux) ->
**install dependencies**
pip install fastapi uvicorn python-dotenv requests langchain langchain-openai ->
**run backend server**
uvicorn main:app --reload ->
**backend will run at** : http://127.0.0.1:8000
**swagger docs** : http://127.0.0.1:8000/docs

**Frontend setup**
cd frontend ->
npm install -> 
npm start ->
**frontend will run at** : http://localhost:3000

Enter a query like : What is the weather in Pune? ->
Click **Ask**
The app responds with "The weather in Pune is clear with a temperature of xx.x°C(depending on the live temp)."




