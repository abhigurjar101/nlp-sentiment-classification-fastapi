import os
os.environ["NLP_USE_TRANSFORMERS"] = "false"
import unittest
from fastapi.testclient import TestClient
from app.main import app

class APITests(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_health_reports_actual_mode(self):
        body = self.client.get("/").json()
        self.assertEqual(body["summarization_mode"], "extractive")
        self.assertEqual(body["sentiment_mode"], "keyword_rules")

    def test_summary_and_sentiment_endpoints(self):
        response = self.client.post("/summarize", json={"text": "First sentence. Second sentence. Third sentence."})
        self.assertEqual(response.status_code, 200)
        body = response.json()
        self.assertEqual(body["summary"], "First sentence. Second sentence.")
        self.assertEqual(body["summary_length"], len(body["summary"]))
        result = self.client.post("/analyze", json={"text": "The app is great"}).json()
        self.assertEqual(result["sentiment"], "POSITIVE")
        self.assertEqual(result["category"], "Product & Engineering")
        # 'good' inside 'goodbye' must not produce positive sentiment.
        self.assertEqual(self.client.post("/analyze", json={"text": "goodbye"}).json()["sentiment"], "NEUTRAL")

    def test_invalid_inputs_are_rejected(self):
        for body in [{"text": " " * 20}, {"text": "x" * 20001},
                     {"text": "A long enough sentence.", "min_length": 100, "max_length": 50},
                     {"text": "A long enough sentence.", "max_length": -1}]:
            self.assertEqual(self.client.post("/summarize", json=body).status_code, 422)
        self.assertEqual(self.client.post("/analyze", json={"text": "   "}).status_code, 422)
