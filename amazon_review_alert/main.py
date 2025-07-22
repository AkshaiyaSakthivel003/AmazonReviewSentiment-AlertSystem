from fetch_reviews import fetch_amazon_reviews
from analyze import analyze_review
from storage import append_to_google_sheet
from alert import send_alert
from utils import calculate_spike

def run_pipeline():
    asin = "B00X4WHP5E"
    reviews = fetch_amazon_reviews(asin)

    results = []
    negatives_today = 0

    for review in reviews:
        sentiment_data = analyze_review(review)
        if sentiment_data['sentiment'] == "Negative":
            negatives_today += 1
        results.append({**sentiment_data, "review": review})

    append_to_google_sheet(results)

    if calculate_spike(negatives_today):
        send_alert(asin, negatives_today)

if __name__ == "__main__":
    run_pipeline()
