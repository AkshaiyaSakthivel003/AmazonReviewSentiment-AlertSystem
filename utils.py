# Simulate spike detection (static threshold)
def calculate_spike(negatives_today, daily_avg=2, threshold=1.5):
    return negatives_today > daily_avg * threshold
