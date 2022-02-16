import requests
from bs4 import BeautifulSoup
import smtplib

url = "https://www.amazon.com/dp/B08G1FP5Z1/psc=1&pd_rd_w=MfthT&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExTkFBNEExUlBONjIyJmVuY3J5cHRlZElkPUEwMjY5MTgzM0ZJMEFETFNZWDdTWiZlbmNyeXB0ZWRBZElkPUEwOTA2MzkzMTVNN1hNWVpVNEQ2TyZ3aWRnZXROYW1lPXNkX29uc2l0ZV9kZXNrdG9wJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
resp = requests.get(url, headers=headers)
soup = BeautifulSoup(resp.text, 'html.parser')
# print(soup.prettify())
trying = soup.find(class_="a-offscreen")
price = trying.getText()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

password = "YOUR PASSWORD"
if price_as_float < 21.1:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="donkeyhottesting@gmail.com", password=password)
        connection.sendmail(
            from_addr="YOUR ADDRESS",
            to_addrs="RECIPENT ADDRESS",
            msg=f"Subject:Amazon price alert! \n\n RC Cars Remote Control Car: Drift High Speed Off Road Stunt Car, Kids Toy with 2 Rechargeable Batteries, 4WD System, Cool Birthday Gifts for Boys Girls Age 6-12 Year Old, Kids Toys \n\nNOW:{price} \n\n{url}"
        )