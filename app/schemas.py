from pydantic import BaseModel, Field, field_validator, model_validator

class SummarizeRequest(BaseModel):
    text: str = Field(..., title="Input Text", description="The text you want to summarize.", min_length=10, max_length=20000)
    max_length: int = Field(130, ge=1, le=512, strict=True, description="Transformer token limit; extractive mode returns up to two sentences.")
    min_length: int = Field(30, ge=1, le=512, strict=True, description="Transformer minimum token count.")

    @field_validator("text")
    @classmethod
    def meaningful_text(cls, value):
        if not value.strip():
            raise ValueError("text must contain non-whitespace characters")
        return value

    @model_validator(mode="after")
    def valid_lengths(self):
        if self.min_length > self.max_length:
            raise ValueError("min_length must not exceed max_length")
        return self

class SummarizeResponse(BaseModel):
    summary: str = Field(..., title="Summary", description="The generated summary.")
    original_length: int = Field(..., title="Original Length", description="Length of original text.")
    summary_length: int = Field(..., title="Summary Length", description="Length of generated summary.")

class SentimentRequest(BaseModel):
    text: str = Field(..., title="Input Text", description="Text to analyze sentiment and category.", min_length=3, max_length=20000)

    @field_validator("text")
    @classmethod
    def meaningful_text(cls, value):
        if not value.strip():
            raise ValueError("text must contain non-whitespace characters")
        return value

class SentimentResponse(BaseModel):
    sentiment: str = Field(..., title="Sentiment", description="Predicted sentiment: POSITIVE, NEGATIVE, or NEUTRAL.")
    confidence: float = Field(..., title="Confidence", ge=0, le=1, description="Uncalibrated heuristic score; not a probability.")
    category: str = Field(..., title="Category", description="Predicted business category.")
