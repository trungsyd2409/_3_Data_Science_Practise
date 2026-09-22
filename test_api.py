from frankfurter import get_rate_trend
rates = get_rate_trend("USD", "AUD", 10)
for date, rate in rates.items():
    print(f"Date: {date}, Rate: {rate}")
