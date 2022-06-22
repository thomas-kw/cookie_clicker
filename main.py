from selenium import webdriver
from selenium.webdriver.common.by import By

import time

chrome_driver_path = "/Users/thomas/PycharmProjects/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

timeout = time.time() + 5
five_min = time.time() + 60 * 5  # 5minutes

# cookie = driver.find_element_by_id("cookie")
# # Get upgrade item ids.
# items = driver.find_elements_by_css_selector("#store div")
# item_ids = [item.get_attribute("id") for item in items]


###################
# while True:
#     cookie.click()
#
#     # Every 5 seconds:
#     if time.time() > timeout:
#
#         # Get all upgrade <b> tags
#         all_prices = driver.find_elements_by_css_selector("#store b")
#         item_prices = []
#
#         # Convert <b> text into an integer price.
#         for price in all_prices:
#             element_text = price.text
#             if element_text != "":
#                 cost = int(element_text.split("-")[1].strip().replace(",", ""))
#                 item_prices.append(cost)
#
#         # Create dictionary of store items and prices
#         cookie_upgrades = {}
#         for n in range(len(item_prices)):
#             cookie_upgrades[item_prices[n]] = item_ids[n]
#
#         # Get current cookie count
#         money_element = driver.find_element_by_id("money").text
#         if "," in money_element:
#             money_element = money_element.replace(",", "")
#         cookie_count = int(money_element)
#
#         # Find upgrades that we can currently afford
#         affordable_upgrades = {}
#         for cost, id in cookie_upgrades.items():
#             if cookie_count > cost:
#                 affordable_upgrades[cost] = id
#
#         # Purchase the most expensive affordable upgrade
#         highest_price_affordable_upgrade = max(affordable_upgrades)
#         print(highest_price_affordable_upgrade)
#         to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
#
#         driver.find_element_by_id(to_purchase_id).click()
#
#         # Add another 5 seconds until the next check
#         timeout = time.time() + 5
#
#     # After 5 minutes stop the bot and check the cookies per second count.
#     if time.time() > five_min:
#         cookie_per_s = driver.find_element_by_id("cps").text
#         print(cookie_per_s)
#         break


#
# current_money_number = int(current_money.text)
# print(current_money_number)


# time.sleep(5)

# if current_money_number >= 5:

cookie = driver.find_element_by_css_selector("#cookie")

# ############
# while True:
#     cookie.click()
#     if time.time() > timeout:
#         buyable = []
#         store = driver.find_elements(By.CSS_SELECTOR, value="#store div")
#         for item in store[:-1]:
#             if item.get_attribute('class') != "grayed":
#                 buyable.append(item)
#         buyable[-1].click()
#         timeout = time.time() + 5
#     if time.time() > five_min:
#         cookie_per_s = driver.find_element(By.ID, value="cps").text
#         print(cookie_per_s)
#         break


####################
#
while True:
    cookie.click()
    if time.time() > timeout:
        # buy_factory = driver.find_element_by_css_selector("#buyFactory")
        buyable = []
        shop_items = driver.find_elements_by_css_selector("#store div")

        for element in shop_items:
            if element.get_attribute('class') != 'grayed':
                buyable.append(element)

        buyable[-1].click()
        timeout = time.time() + 5

        # print(buyable)
        # buyable[-1].click()

        # current_money = driver.find_element_by_css_selector("#money")
        # current_money_number = current_money.text
        # current_money_format = int(current_money_number.replace(",", ""))

        # if buy_factory.get_attribute('class') != "grayed":
        #     buy_factory.click()
        #     timeout = time.time() + 5
