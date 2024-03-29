import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_driver_path = r"C:\Users\andre.a.filho\Documents\selenium_driver\chromedriver.exe"

service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

#driver.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")
#price = driver.find_element(By.ID, "priceblock_ourprice")
#print(price)

#driver.close()

#Challenge 1
"""
driver.get("https://www.python.org/")
event_times = driver.find_elements(
    By.CSS_SELECTOR,
    "div.medium-widget.event-widget.last time"
)
event_names = driver.find_elements(
    By.CSS_SELECTOR,
    "div.medium-widget.event-widget.last li a"
)
events = {}
for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }
print(events)
"""
"""
driver.get("https://en.wikipedia.org/wiki/Main_Page")
statistics = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# statistics.click()
search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)
time.sleep(5)
"""
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")
items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]
timeout = time.time() + 5
five_min = time.time() + 60*5

while True:
    cookie.click()

    if time.time() > timeout:
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = []

        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]
        money_element = driver.find_element(By.ID, "money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element(By.ID, to_purchase_id).click()

        timeout = time.time() + 5

    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, "cps").text
        print(cookie_per_s)
        break

driver.close()
driver.quit()