from pydantic import BaseModel, Field

class SummarizeRequest(BaseModel):
    text: str = Field(..., title="Input Text", description="The text you want to summarize.", min_length=10)
    max_length: int = Field(130, title="Maximum Length", description="Maximum length of the summary.")
    min_length: int = Field(30, title="Minimum Length", description="Minimum length of the summary.")

class SummarizeResponse(BaseModel):
    summary: str = Field(..., title="Summary", description="The generated summary.")
    original_length: int = Field(..., title="Original Length", description="Length of original text.")
    summary_length: int = Field(..., title="Summary Length", description="Length of generated summary.")

class SentimentRequest(BaseModel):
    text: str = Field(..., title="Input Text", description="Text to analyze sentiment and category.", min_length=3)

class SentimentResponse(BaseModel):
    sentiment: str = Field(..., title="Sentiment", description="Predicted sentiment: POSITIVE, NEGATIVE, or NEUTRAL.")
    confidence: float = Field(..., title="Confidence", description="Confidence score between 0 and 1.")
    category: str = Field(..., title="Category", description="Predicted business category.")
