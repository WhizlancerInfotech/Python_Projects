from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get("https://www.amazon.com/dp/B08N5WRWNW")

soup = BeautifulSoup(driver.page_source, "html.parser")
title = soup.find("span", {"id": "productTitle"}).text.strip()
price = soup.find("span", {"class": "a-offscreen"}).text

print("Product:", title)
print("Price:", price)

driver.quit()
