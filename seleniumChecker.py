from selenium import webdriver
import time
import random
import collections

data = collections.OrderedDict()
data["ps5_amazon"] = {
    "url": "https://www.amazon.co.uk/gp/product/B08H95Y452/",
    "cookieId": "sp-cc-accept",
    "addToBasketId": "add-to-cart-button",
    "noInsuranceId": "attachSiNoCoverage-announce"
}
data["ps5_smyths"] = {
    "url": "https://www.smythstoys.com/uk/en-gb/video-games-and-tablets/playstation-5/playstation-5-consoles/playstation-5-console/p/191259",
    "cookieClass": "cookie-btn-yes",
    "addToBasketId": "addToCartButton"
}
print(data)

# best to start up all tabs first and refresh individually
browser = webdriver.Chrome("./chromedriver")

for key, value in data.items():
    print(key)
    # ps5 amazon
    if key == "ps5_amazon":
        browser.get(data[key]["url"])
        accept_cookies = browser.find_element_by_id(
            data[key]['cookieId']).click()
        try:
            add_to_basket = browser.find_element_by_id(
                'add-to-cart-button').click()
            wait_time = random.randrange(1, 2)
            time.sleep(wait_time)
            browser.find_element_by_id(data[key]["noInsuranceId"]).click()
        except:
            continue

        # refresh_wait_time = random.randrange(10, 15)
        # browser.refresh()
    # xbox x amazon
    # if key == "xboxx_amazon":

    # ps5 smyths
    if key == "ps5_smyths":
        browser.execute_script("window.open('about:blank', 'tab2');")
        browser.switch_to.window("tab2")
        browser.get(data[key]["url"])
        browser.find_element_by_class_name(data[key]["cookieClass"]).click()

    #     # xbox x smyths
    # if key == ps5amazon:

    #     # ps5 argos
    # if key == ps5amazon:

    #     # xbox x argos
    # if key == ps5amazon:

    #     # ps5 game
    # if key == ps5amazon:

    #     # xbox x game
    # if key == ps5amazon:

        # # need to find the input button with id "add-to-cart-button" and name "submit.add-to-cart"
        # try:
        #     add_to_basket = browser.find_element_by_id('add-to-cart-button').click()
        #     noinsurance_wait_time = random.randrange(1, 2)
        #     time.sleep(wait_time)
        #     browser.find_element_by_id('attachSiNoCoverage-announce').click()
        # except:
        #     refresh_wait_time = random.randrange(10, 15)
        #     browser.refresh()

        # browser.execute_script("window.open('about:blank', 'tab2');")
        # browser.switch_to.window("tab2")
        # browser.get('')
        # browser.find_element_by_class('').click()
