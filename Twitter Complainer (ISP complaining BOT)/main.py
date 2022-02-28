from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from InternetSpeedTwitterBot import InternetSpeedTwitterBot

s=Service("YOUR CHROME DRIVER FILE PATH")
driver = webdriver.Chrome(service=s)

PROMISED_DOWN = 100   # your contract download speed
PROMISED_UP = 70    # your contract upload speed
TWITTER_MAIL = "YOUR MAIL"
TWITTER_PASS = "YOUR PASSWORD"
net_url = "https://www.speedtest.net/"
twitter = "https://twitter.com/?lang=en"

bot = InternetSpeedTwitterBot(s, driver, PROMISED_UP, PROMISED_DOWN)
bot.get_internet_speed(net_url)
bot.tweet_at_provider(twitter, TWITTER_MAIL, TWITTER_PASS)