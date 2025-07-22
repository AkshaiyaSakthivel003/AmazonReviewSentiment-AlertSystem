from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer # type: ignore

analyzer = SentimentIntensityAnalyzer()

def analyze_review(review_text):
    scores = analyzer.polarity_scores(review_text)
    compound = scores['compound']

    if compound >= 0.05:
        sentiment = "Positive"
        issue = ""
    elif compound <= -0.05:
        sentiment = "Negative"
        # Simple heuristic for issue detection
        if any(word in review_text.lower() for word in ["not", "bad", "stopped", "disappoint"]):
            issue = "Product defect or complaint"
        else:
            issue = ""
    else:
        sentiment = "Neutral"
        issue = ""

    return {"sentiment": sentiment, "issue": issue}
