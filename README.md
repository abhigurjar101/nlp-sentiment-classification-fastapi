# NLP API: summarization and sentiment baseline

A FastAPI demonstration with text summarization, keyword-based sentiment, and category tags. Default mode runs without model downloads. Optional DistilBART summarization can be enabled explicitly.

## Run

```bash
git clone https://github.com/abhigurjar101/nlp-sentiment-classification-fastapi.git
cd nlp-sentiment-classification-fastapi
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
python -m unittest discover -s tests -v
uvicorn app.main:app --reload --port 8000
```

Open `http://localhost:8000/docs`. `test_nlp_api.py` prints model-level examples; it is not the API regression suite.

## Endpoints

| Method | Path | Behavior |
|---|---|---|
| GET | `/` | Reports health and active summarization/sentiment modes |
| POST | `/summarize` | Takes `text`, optional `min_length` and `max_length`; returns summary and character counts |
| POST | `/analyze` | Takes `text`; returns rule sentiment, heuristic confidence and category |

```bash
curl -X POST http://localhost:8000/analyze -H 'Content-Type: application/json' -d '{"text":"The app is great"}'
```

Default summarization returns up to two period-separated sentences. Length settings control the optional transformer's token counts; they do not limit extractive output. Input is limited to 20,000 characters. Blank text and invalid length ranges return 422.

## Optional transformer summarization

Install `requirements-transformers.txt`, then start with `NLP_USE_TRANSFORMERS=true uvicorn app.main:app --port 8000`. This downloads `sshleifer/distilbart-cnn-12-6` on first use and requires memory and disk space. Initialization fails visibly if the model cannot load. Sentiment remains a keyword baseline in both modes.

## Docker

```bash
docker build -t nlp-demo .
docker run --rm -p 8000:8000 nlp-demo
```

The default image runs the offline baseline and does not download a model during build.

## Limits and evaluation

Sentiment does not use a trained classifier. Confidence is an uncalibrated heuristic, not a probability; negation, sarcasm, and domain shift are not handled. Category matching uses substring rules. No latency, throughput, precision, recall, F1, or production-readiness result is claimed. Evaluate a labeled dataset and add authentication, monitoring, and load tests before deployment.

`app/` contains routes, schemas, and the inference baseline. `tests/` exercises actual API responses, input rejection and whole-word sentiment matching. GitHub Actions runs these tests without external model calls.

[Abhi Kumar Gurjar](https://www.linkedin.com/in/abhigurjar)
