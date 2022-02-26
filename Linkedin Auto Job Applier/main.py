import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

url = "https://www.linkedin.com/jobs/search/?f_AL=true&keywords=junior%20developer%20python&sortBy=R"
username = "YOUR USERNAME"
password = "YOUR PASSWORD"

s=Service("YOURPATH/chromedriver")
driver = webdriver.Chrome(service=s)

#Open the url and pressing sign in button
driver.get(url)
time.sleep(3)
sign_in_btn = driver.find_element(By.CLASS_NAME, "cta-modal__primary-btn").click()

# Filling username & password and signing in
username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")
username_field.send_keys(username)
password_field.send_keys(password)
sign_in_btn2 = driver.find_element(By.CLASS_NAME, "login__form_action_container").click()
time.sleep(4)

# Clicking on the newest jobs result
first_job = driver.find_element(By.CSS_SELECTOR, ".jobs-search-results__list li").click()
time.sleep(5)
# Apply for the job
apply_btn = driver.find_element(By.CLASS_NAME, "jobs-apply-button--top-card").click()

