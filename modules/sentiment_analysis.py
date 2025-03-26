from transformers import pipeline

# Load a model that supports Positive, Negative, and Neutral classification
sentiment_pipeline = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")

def perform_sentiment_analysis(text):
    result = sentiment_pipeline(text)[0]
    
    # Convert model labels to readable sentiment categories
    if result["label"] == "LABEL_0":
        sentiment = "NEGATIVE"
    elif result["label"] == "LABEL_1":
        sentiment = "NEUTRAL"
    else:
        sentiment = "POSITIVE"

    return sentiment, result["score"]
