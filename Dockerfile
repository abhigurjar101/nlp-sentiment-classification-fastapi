FROM python:3.10-slim

WORKDIR /code

# Install torch CPU version specifically to save container size
RUN pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu

# Install other requirements
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir -r /code/requirements.txt

# Pre-download the model during image build so it starts fast
# We use a smaller distilbart model for CPU efficiency
RUN python -c "from transformers import pipeline; pipeline('summarization', model='sshleifer/distilbart-cnn-12-6')"

# Copy the application code
COPY ./app /code/app

# Command to run the server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
