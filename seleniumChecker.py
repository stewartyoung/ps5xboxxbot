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
data["xboxx_amazon"] = {
    'url': "https://www.amazon.co.uk/Xbox-Series-S/dp/B08H93GKNJ/ref=twister_B08JHLMGZB?_encoding=UTF8&psc=1",
    'switchToXboxXid': "a-autoid-15-announce",

}
data["ps5_smyths"] = {
    "url": "https://www.smythstoys.com/uk/en-gb/video-games-and-tablets/playstation-5/playstation-5-consoles/playstation-5-console/p/191259",
    "cookieClass": "cookie-btn-yes",
    "addToBasketId": "addToCartButton"
}
data["xboxx_smyths"] = {
    "url": "https://www.smythstoys.com/uk/en-gb/video-games-and-tablets/xbox-gaming/xbox-series-x-%7c-s/xbox-series-x-%7c-s-consoles/xbox-series-x-1tb-console/p/192012",
    "cookieClass": "cookie-btn-yes",
    "addToBasketId": "addToCartButton"
}
data["ps5_game"] = {
    "url": "https://www.game.co.uk/playstation-5",
    "cookieClass": "cookie-btn-yes",
    "addToBasketId": "addToCartButton"
}
data["xboxx_game"] = {
    "url": "https://www.smythstoys.com/uk/en-gb/video-games-and-tablets/xbox-gaming/xbox-series-x-%7c-s/xbox-series-x-%7c-s-consoles/xbox-series-x-1tb-console/p/192012",
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
            print(key + " not in stock")
            continue

    # xbox x amazon
    if key == "xboxx_amazon":
        browser.execute_script("window.open('about:blank', 'tab2');")
        browser.switch_to.window("tab2")
        browser.get(data[key]["url"])
        # change from xbox remote to xbox series x tab
        browser.find_element_by_id(data[key]["switchToXboxXid"]).click()
        try:
            add_to_basket = browser.find_element_by_id(
                'add-to-cart-button').click()
            wait_time = random.randrange(1, 2)
            time.sleep(wait_time)
            browser.find_element_by_id(data[key]["noInsuranceId"]).click()
        except:
            print(key + " not in stock")
            continue

    # ps5 smyths
    if key == "ps5_smyths":
        browser.execute_script("window.open('about:blank', 'tab3');")
        browser.switch_to.window("tab3")
        browser.get(data[key]["url"])
        # give it two secs to show cookie selector
        time.sleep(2)
        browser.find_element_by_class_name(data[key]["cookieClass"]).click()
        try:
            add_to_basket = browser.find_element_by_id(
                data[key]['addToBasketId']).click()
        except:
            print(key + " not in stock")
            continue

    # xbox x smyths
    if key == "xboxx_smyths":
        browser.execute_script("window.open('about:blank', 'tab4');")
        browser.switch_to.window("tab4")
        browser.get(data[key]["url"])
        try:
            add_to_basket = browser.find_element_by_id(
                data[key]['addToBasketId']).click()
        except:
            print(key + " not in stock")
            continue

    # ps5 game
    if key == "ps5_game":
        browser.execute_script("window.open('about:blank', 'tab4');")
        browser.switch_to.window("tab4")
        browser.get(data[key]["url"])

    # xbox x game
    # if key == ps5amazon:

    #     # ps5 argos
    # if key == ps5amazon:

    #     # xbox x argos
    # if key == ps5amazon:
