SHL Conversational Assessment Recommender
Overview

This project was built for the SHL AI Intern Assignment.

The goal of the project is to help recruiters and hiring managers find suitable SHL assessments through a conversational interface instead of using traditional keyword searches.

The system accepts hiring-related queries such as:

“Hiring a Java developer”
“Need assessments for leadership roles”
“Looking for communication and aptitude tests”

Based on the user query, the system retrieves and recommends relevant SHL assessments.

The project uses:

FastAPI for backend API development
FAISS for vector similarity search
Sentence Transformers for embeddings
Python for implementation
Features
Conversational SHL assessment recommendation system
FastAPI backend with REST API endpoints
Vector-based retrieval using FAISS
Clarification handling for vague queries
Structured JSON responses
Duplicate recommendation filtering
Swagger API documentation support
Tech Stack
Technology	Usage
Python	Core programming language
FastAPI	Backend API framework
FAISS	Vector similarity search
Sentence Transformers	Text embeddings
Render	Deployment platform
Project Structure
shl-ai-recommender/
│
├── app.py
├── recommender.py
├── build_index.py
├── scraper.py
├── prompts.py
├── utils.py
├── catalog.json
├── index.faiss
├── requirements.txt
├── Procfile
├── README.md
└── .gitignore
How It Works
SHL assessment data is stored in catalog.json
Sentence embeddings are generated using Sentence Transformers
FAISS is used to perform vector similarity search
FastAPI exposes API endpoints
User queries are matched with relevant assessments
Recommendations are returned in JSON format
Installation
Clone Repository
git clone https://github.com/Nikhil30072/shl-ai-recommender.git

cd shl-ai-recommender
Install Dependencies
pip install -r requirements.txt
Run the Project
Step 1 — Build FAISS Index
python build_index.py
Step 2 — Start FastAPI Server
uvicorn app:app --reload
Step 3 — Open Swagger Documentation

Open:

http://127.0.0.1:8000/docs
API Endpoints
GET /health

Checks whether the API is running properly.

Response
{
  "status": "ok"
}
POST /chat

Accepts conversation messages and returns SHL assessment recommendations.

Example Request
{
  "messages": [
    {
      "role": "user",
      "content": "Hiring Java developer with leadership skills"
    }
  ]
}
Example Response
{
  "reply": "Here are recommended SHL assessments.",
  "recommendations": [
    {
      "name": "Core Java Assessment",
      "url": "https://www.shl.com",
      "test_type": "K"
    }
  ],
  "end_of_conversation": false
}
Evaluation

The project was tested for:

recommendation relevance
duplicate filtering
clarification handling
response formatting
retrieval quality

Future Improvements
Better conversational memory
Real SHL catalog scraping
Improved ranking system
Assessment comparison support
Better prompt engineering

Author:
Nikhil Abboju
