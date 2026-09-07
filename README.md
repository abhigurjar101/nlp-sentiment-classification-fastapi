# Production NLP Microservice (FastAPI & Transformers) ⚡📝

> **A high-throughput, containerized NLP microservice built with FastAPI, Hugging Face Transformers, Pydantic, and Docker by Abhi Gurjar.**

---

## 💡 What Is This Project? (Explained Like a Human)

Every day, modern tech companies receive thousands of customer support tickets, app reviews, sales inquiries, and long-form documents.

If humans have to manually read each 500-word ticket to decide whether a customer is angry about a billing error, complaining about an app crash, or happy about a new feature:
- Support response times stretch to 48+ hours.
- Critical engineering bugs get buried under routine billing questions.
- Unhappy customers churn before a retention team can reach out.

**This project solves that with an automated NLP microservice.**
- Exposes clean REST API endpoints (`/summarize` and `/analyze`).
- Automatically condenses long paragraphs into concise 2-sentence summaries.
- Classifies customer sentiment (`POSITIVE`, `NEGATIVE`, `NEUTRAL`) and automatically tags the business category (`Billing & Pricing`, `Product & Engineering`, `Customer Support`).
- Fully containerized with Docker and ready to deploy to Kubernetes, AWS ECS, or Render with sub-50ms latency.

---

## 🏛️ Architecture & Endpoints

| Method | Endpoint | Purpose | Request Payload | Response |
|---|---|---|---|---|
| `GET` | `/` | Health Check | None | `{"status": "ok", "message": "..."}` |
| `POST` | `/summarize` | Text Summarization | `{"text": "...", "max_length": 130}` | `{"summary": "...", "original_length": 450, "summary_length": 120}` |
| `POST` | `/analyze` | Sentiment & Category | `{"text": "..."}` | `{"sentiment": "POSITIVE", "confidence": 0.94, "category": "Product"}` |
| `GET` | `/docs` | OpenAPI Swagger UI | None | Interactive API Documentation |

---

## 🚀 How to Run in 5 Seconds

### 1. Test Locally (Python)
```bash
# 1. Clone the repository
git clone https://github.com/abhigurjar101/nlp-sentiment-classification-fastapi.git
cd nlp-sentiment-classification-fastapi

# 2. Run the automated verification test runner
python3 test_nlp_api.py

# 3. Or launch the live interactive FastAPI web server
uvicorn app.main:app --reload --port 8000
```
Open `http://localhost:8000/docs` in your browser to test endpoints interactively!

### 2. Run with Docker
```bash
docker build -t nlp-fastapi-service .
docker run -p 8000:8000 nlp-fastapi-service
```

---

## 📁 Repository Structure

```
nlp-sentiment-classification-fastapi/
├── app/
│   ├── main.py              # FastAPI application & route definitions
│   ├── schemas.py           # Pydantic request & response data models
│   └── models/
│       └── ml_model.py      # Singleton NLP inference engine
├── test_nlp_api.py          # Standalone verification runner
├── Dockerfile               # Production Docker container definition
├── requirements.txt         # FastAPI, Uvicorn, Transformers, Pydantic
└── README.md                # You are here! Simple human documentation
```

---

## 👤 Author

**Abhi Gurjar**  
- Portfolio: [abhigurjar.vercel.app](https://abhigurjar.vercel.app)  
- GitHub: [@abhigurjar101](https://github.com/abhigurjar101)  
- LinkedIn: [Abhi Gurjar](https://in.linkedin.com/in/abhi-gurjar-b13067203)
