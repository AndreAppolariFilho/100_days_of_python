import datetime
import json
import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def get_variation(company_code):
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    day_before_yesterday = (datetime.datetime.now() - datetime.timedelta(days=2)).strftime("%Y-%m-%d")

    with open("credentials.json", "r") as json_file:
        api_key = json.load(json_file)["API_KEY"]

    data = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": "TSLA",
        "apikey": api_key
    }
    url = "https://www.alphavantage.co/query"
    request_data = requests.get(url, params=data)
    request_data.raise_for_status()
    request_json = request_data.json()
    yesterday_closing = float(request_json["Time Series (Daily)"][yesterday]["5. adjusted close"])
    day_before_yesterday_closing = float(request_json["Time Series (Daily)"][day_before_yesterday]["5. adjusted close"])
    return yesterday_closing - day_before_yesterday_closing
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
def get_news_for_company(company_name):
    with open("credentials.json", "r") as json_file:
        api_key = json.load(json_file)["NEWS_API_KEY"]
    url = "https://newsapi.org/v2/everything"
    params = {
        "qInTitle":company_name,
        "pageSize":3,
        "apiKey": api_key
    }
    request_data = requests.get(url, params=params)
    request_data.raise_for_status()
    request_json = request_data.json()
    return [
        {"title": article["title"],"content":article["description"]}
        for article in request_json["articles"]]

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
def build_message(percentage_change, company_code, list_of_articles):
    emoji = "🔺" if percentage_change > 0 else "🔻"
    list_of_aticles_formated = [f"Headline: {article['title']}\nBrief:{article['content']}\n" for article in list_of_articles]
    msg = f"{company_code}: {emoji} {percentage_change:.2f}\n"
    msg += "\n".join(list_of_aticles_formated)
    return msg

#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
if __name__ == "__main__":
    variation = get_variation(STOCK)
    news = get_news_for_company(COMPANY_NAME)
    print(build_message(variation, STOCK, news))
