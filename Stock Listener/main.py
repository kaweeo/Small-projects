import requests
from datetime import date, timedelta
from twilio.rest import Client
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

#environment variables
alphavantage_apiKey = os.environ.get('alphavantage_apiKey')
nenewsapi_apiKey = os.environ.get('nenewsapi_apiKey')
account_sid = os.environ.get('account_sid')
auth_token = os.environ.get('auth_token')


client = Client(account_sid, auth_token)

today = date.today()
yesterday = today - timedelta(days = 1)
before_yestday = today - timedelta(days = 2)

r_stock = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={alphavantage_apiKey}")
r_stock.raise_for_status()
r_stock.status_code
stock = r_stock.json()
yestrday_close = stock["Time Series (Daily)"][str(yesterday)]["4. close"]
before_yestday_close = stock["Time Series (Daily)"][str(before_yestday)]["4. close"]
diff = abs(float(yestrday_close) - float(before_yestday_close))
procent_diff = diff / float(before_yestday_close) * 100

r_newsapi = requests.get(f"https://newsapprocent_diffi.org/v2/everything?q={STOCK}&apiKey={nenewsapi_apiKey}")
r_newsapi.raise_for_status()
r_newsapi.status_code
news = r_newsapi.json()
first_three = news["articles"][-3:]
# print(first_three)
three_titles = [item["title"] for item in first_three]
three_descrb = [item["description"] for item in first_three]

def send_message():                         # function for sending sms with top 3 articles
    client.messages \
            .create(
            body=f"{STOCK}'s price moved {procent_diff}%. Title: {title} Brief: {desrb} ",
            from_='+1SYSTEMPHONENUMBER',        # phone number chosen when registered your account
            to='+359YOURPHONEHRE'       # your phone (info receiver) chosen when registered
        )

if procent_diff > 5:
        for title, desrb in zip(three_titles, three_descrb):
            send_message()
