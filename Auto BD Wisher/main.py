import datetime as dt
import random
import smtplib


df = pd.read_csv("birthdays.csv")
data_month = df["month"]
data_day = df["day"]
now = dt.datetime.now()
month = now.month
day = now.day

bd_dict = df.to_dict(orient="records")

for dict in bd_dict:
    if dict["month"] == month and dict["day"] == day:
        bd_mail = dict["email"]
        bd_name = dict["name"]
        print(bd_name, bd_mail)

with open("letter_templates/letter_1.txt", "r") as f1:
    f1data = f1.read()
with open("letter_templates/letter_2.txt", "r") as f2:
    f2data = f2.read()
with open("letter_templates/letter_3.txt", "r") as f3:
    f3data = f3.read()

wishes = [f1data, f2data, f3data]
the_wish = random.choice(wishes)
try:
    the_wish = the_wish.replace("[NAME]", bd_name)
    print(the_wish)
except NameError:
    pass
else:
    password = "DHT3210123"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="donkeyhottesting@gmail.com", password=password)
        connection.sendmail(
            from_addr="donkeyhottesting@gmail.com",
            to_addrs=bd_mail,
            msg=f"Subject:Happy B-DAY \n\n {the_wish}"
        )
