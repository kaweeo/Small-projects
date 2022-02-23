import threading

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from threading import Timer
import time

s=Service("/YOUR-PATH/chromedriver/chromedriver")
driver = webdriver.Chrome(service=s)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")
cookie.click()

cursor_cost = driver.find_element(By.ID, "buyCursor")
grandma_cost = driver.find_element(By.ID, "buyGrandma")
factory_cost = driver.find_element(By.ID, "buyFactory")
mine_cost = driver.find_element(By.ID, "buyMine")
shipment = driver.find_element(By.ID, "buyShipment")
alchemy = driver.find_element(By.ID, "buyAlchemy lab")
portal = driver.find_element(By.ID, "buyPortal")
time_machine = driver.find_element(By.ID, "buyTime machine")


costs = {
    cursor_cost: 15,
    grandma_cost: 100,
    factory_cost: 500,
    mine_cost: 2000,
    shipment: 7000,
    alchemy: 50000,
    portal: 1000000,
    time_machine: 123456789,
}

def money_check():
    money_el = driver.find_element(By.ID, "money")
    money = money_el.text
    money = int(money.replace(",", ""))
    print(money)
    return money

def buy_checker():
    time.sleep(5)
    global money
    to_buy = cursor_cost
    availables = []
    for value in costs.values():
        if money > value:
            availables.append(value)
            the_best_buy = availables[-1]
            to_buy = [key for key, value in costs.items() if value == the_best_buy]
        else:
            pass
    to_buy.click()


while True:
    money = money_check()
    buy_checker()
    cookie.click()



