from selenium import webdriver
import time
from datetime import datetime
import random
import collections
# import smtplib for actual email sending function
import smtplib
# import email modules required
from email.mime.text import MIMEText

# create a function to send an email with the url if something has come in stock
# and may be in the basket
gmail_user = input("Input your email: ")
gmail_password = input("Input your email password: ")


def sendSuccessEmail(subject, url):
    datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    msg = MIMEText(url + "\n\nCongrats from the console bot!")
    msg['Subject'] = subject

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(gmail_user,
                    [gmail_user], msg.as_string())
    server.quit()


data = collections.OrderedDict()
# test amazon on xbox one
# data['ps5_amazon'] = {
#     "url": "https://www.amazon.co.uk/Microsoft-Xbox-One-1TB-Console/dp/B01M5FMXHZ/",
#     "cookieId": "sp-cc-accept",
#     "addToBasketId": "add-to-cart-button",
#     "noInsuranceId": "attachSiNoCoverage-announce"
# }
data["ps5_amazon"] = {
    "url": "https://www.amazon.co.uk/PlayStation-9395003-5-Console/dp/B08H95Y452/",
    "cookieId": "sp-cc-accept",
    "addToBasketId": "add-to-cart-button",
    "noInsuranceId": "attachSiNoCoverage-announce"
}
data["xboxx_amazon"] = {
    'url': "https://www.amazon.co.uk/Xbox-Series-S/dp/B08H93GKNJ/ref=twister_B08JHLMGZB?_encoding=UTF8&psc=1",
    'switchToXboxXid': "a-autoid-15-announce",
    "addToBasketId": "add-to-cart-button",
    "noInsuranceId": "attachSiNoCoverage-announce"

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
    "anchorBefore": "/en/digital/?attributeName1=Platform&attributeValue1=4294954047&cm_sp=PlayStationHardwarePage-_-Digital-_-ShopAll",
    "cookieClass": "accept",
    "basketClass": 'addToBasket'
}
data["xboxx_game"] = {
    "url": "https://www.game.co.uk/webapp/wcs/stores/servlet/HubArticleView?hubId=2626751&articleId=2626751&catalogId=10201&langId=44&storeId=10151",
    "anchorBefore": "/en/accessories/xbox-series?cm_sp=XboxSeriesXHardwarePage-_-Accessories-_-shopall",
    "basketClass": 'addToBasket'
}

data["xboxs_microsoft"] = {
    "url": "https://www.microsoft.com/en-gb/p/xbox-series-x/942j774tp9jn?activetab=pivot%3aoverviewtab",
    'configureButton': "buttons_ConfigureDeviceButton"
}

# data["ps4_very"] = {
#     "url": "hi"
# }

# data["xboxx_very"] = {
#     "url": "hi"
# }

# data["ps4_argos"] = {
#     "url": "hi"
# }

# data["xboxx_argos"] = {
#     "url": "hi"
# }

# data["xboxs_currys"] = {
#     "url": "https://www.currys.co.uk/gbuk/gaming/console-gaming/consoles/microsoft-xbox-series-s-512-gb-ssd-10205195-pdt.html"
# }

# best to start up all tabs first and refresh individually
browser = webdriver.Chrome("chromedriver")

for key, value in data.items():
    print(key)
    # ps5 amazon
    if key == "ps5_amazon":
        browser.get(data[key]["url"])
        accept_cookies = browser.find_element_by_id(
            data[key]['cookieId']).click()
        time.sleep(random.randrange(1, 2))
        try:
            add_to_basket = browser.find_element_by_id(
                'add-to-cart-button').click()
            time.sleep(random.randrange(2, 3))
            browser.find_element_by_id(data[key]["noInsuranceId"]).click()
            sendSuccessEmail(subject=key + " added to basket!!",
                             url=data[key]["url"])
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
            time.sleep(random.randrange(2, 3))
            browser.find_element_by_id(data[key]["noInsuranceId"]).click()
            sendSuccessEmail(subject=key + " added to basket!!",
                             url=data[key]["url"])
        except:
            print(key + " not in stock")
            continue

    # ps5 smyths
    if key == "ps5_smyths":
        browser.execute_script("window.open('about:blank', 'tab3');")
        browser.switch_to.window("tab3")
        browser.get(data[key]["url"])
        # give it three secs to show cookie selector
        time.sleep(3)
        browser.find_element_by_class_name(data[key]["cookieClass"]).click()
        time.sleep(random.randrange(1, 2))
        try:
            add_to_basket = browser.find_element_by_id(
                data[key]['addToBasketId']).click()
            sendSuccessEmail(subject=key + " added to basket!!",
                             url=data[key]["url"])
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
            sendSuccessEmail(subject=key + " added to basket!!",
                             url=data[key]["url"])
        except:
            print(key + " not in stock")
            continue

    # ps5 game
    if key == "ps5_game":
        browser.execute_script("window.open('about:blank', 'tab5');")
        browser.switch_to.window("tab5")
        browser.get(data[key]["url"])
        time.sleep(random.randrange(3, 4))
        # # close cookies policy
        browser.find_element_by_class_name(data[key]["cookieClass"]).click()
        # try clicking on console page
        anchors = browser.find_elements_by_xpath("//a")
        shopall = browser.find_element_by_xpath(
            '//a[@href="' + data[key]["anchorBefore"]+'"]')
        # ps5 anchor is after the shop all anchor
        shopAllIndex = anchors.index(shopall)
        buy = anchors[shopAllIndex+1]
        if buy.get_attribute("href") != "javascript:void(0);":
            try:
                # try clicking on console page
                buy.click()
                time.sleep(random.randrange(2, 3))
                add_to_basket = browser.find_element_by_class_name(
                    data[key]["basketClass"]).click()
                sendSuccessEmail(subject=key + " added to basket!!",
                                 url=data[key]["url"])
            except:
                print(key + " not in stock")
                continue
        else:
            print(key + " not in stock javascript:void(0)")
            continue

    # xbox x game
    if key == "xboxx_game":
        browser.execute_script("window.open('about:blank', 'tab6');")
        browser.switch_to.window("tab6")
        browser.get(data[key]["url"])
        time.sleep(random.randrange(3, 4))
        # try clicking on console page
        anchors = browser.find_elements_by_xpath("//a")
        shopall = browser.find_element_by_xpath(
            '//a[@href="' + data[key]["anchorBefore"]+'"]')
        # print(anchors)
        # print(len(anchors))
        # xboxx anchor is after the shop all anchor
        shopAllIndex = anchors.index(shopall)
        buy = anchors[shopAllIndex+1]
        if buy.get_attribute("href") != "javascript:void(0);":
            try:
                # try clicking on console page
                buy.click()
                time.sleep(random.randrange(2, 3))
                add_to_basket = browser.find_element_by_class_name(
                    data[key]["basketClass"]).click()
                sendSuccessEmail(subject=key + " added to basket!!",
                                 url=data[key]["url"])
            except:
                print(key + " not in stock")
                continue
        else:
            print(key + " not in stock javascript:void(0)")
            continue

    # xbox s microsoft
    if key == "xboxs_microsoft":
        browser.execute_script("window.open('about:blank', 'tab7');")
        browser.switch_to.window("tab7")
        browser.get(data[key]["url"])
        time.sleep(random.randrange(1, 2))
        try:
            time.sleep(random.randrange(2, 3))
            if browser.find_element_by_id(
                    data[key]["configureButton"]).is_enabled():
                configure = browser.find_element_by_id(
                    data[key]["configureButton"]).click()
                if browser.find_element_by_xpath('//button[@role="option"]').is_enabled():
                    browser.find_element_by_xpath('//button[@role="option"]').click()
                    if browser.find_element_by_class_name(
                    'c-button').is_enabled():
                        add_to_cart = browser.find_element_by_class_name(
                    'c-button').is_enabled()
                        sendSuccessEmail(subject=key + " added to basket!!",
                                url=data[key]["url"])
            else:
                raise Exception('configure button not clickable')
        except:
            print(key + " not in stock")
            continue

i = 0
while i >= 0:
    # loop over the tabs refreshing repeatedly

    if i == 0:
        browser.switch_to.window(browser.window_handles[i])
        # browser.switch_to.window("tab"+str(i+1))
        browser.refresh()
        time.sleep(random.randrange(1, 2))
        try:
            add_to_basket = browser.find_element_by_id(
                'add-to-cart-button').click()
            time.sleep(random.randrange(1, 2))
            browser.find_element_by_id(
                list(data.items())[i][1]["noInsuranceId"]).click()
            sendSuccessEmail(subject=list(data.items())[i][0] + " added to basket!!",
                             url=list(data.items())[i][1]["url"])
            i += 1
        except:
            print(list(data.items())[i][0] + " not in stock")
            i += 1
            continue

    if i == 1:
        browser.switch_to.window(browser.window_handles[i])
        browser.refresh()
        time.sleep(random.randrange(1, 2))
        # change from xbox remote to xbox series x tab
        browser.find_element_by_id(
            list(data.items())[i][1]["switchToXboxXid"]).click()
        try:
            add_to_basket = browser.find_element_by_id(
                'add-to-cart-button').click()
            time.sleep(random.randrange(1, 2))
            browser.find_element_by_id(
                list(data.items())[i][1]["noInsuranceId"]).click()
            sendSuccessEmail(subject=list(data.items())[i][0] + " added to basket!!",
                             url=list(data.items())[i][1]["url"])
            i += 1
        except:
            print(list(data.items())[i][0] + " not in stock")
            i += 1
            continue

    if i == 2:
        browser.switch_to.window(browser.window_handles[i])
        browser.refresh()
        time.sleep(random.randrange(1, 2))
        try:
            add_to_basket = browser.find_element_by_id(
                list(data.items())[i][1]['addToBasketId']).click()
            sendSuccessEmail(subject=list(data.items())[i][0] + " added to basket!!",
                             url=list(data.items())[i][1]["url"])
            i += 1
        except:
            print(list(data.items())[i][0] + " not in stock")
            i += 1
            continue

    if i == 3:
        browser.switch_to.window(browser.window_handles[i])
        browser.refresh()
        time.sleep(random.randrange(1, 2))
        try:
            add_to_basket = browser.find_element_by_id(
                list(data.items())[i][1]['addToBasketId']).click()
            sendSuccessEmail(subject=list(data.items())[i][0] + " added to basket!!",
                             url=list(data.items())[i][1]["url"])
            i += 1
        except:
            print(list(data.items())[i][0] + " not in stock")
            i += 1
            continue

    if i == 4:
        browser.switch_to.window(browser.window_handles[i])
        browser.refresh()
        time.sleep(random.randrange(3, 4))
        anchors = browser.find_elements_by_xpath("//a")
        shopall = browser.find_element_by_xpath(
            '//a[@href="' + list(data.items())[i][1]["anchorBefore"]+'"]')
        # ps5 anchor is after the shop all anchor
        shopAllIndex = anchors.index(shopall)
        buy = anchors[shopAllIndex+1]
        if buy.get_attribute("href") != "javascript:void(0);":
            try:
                # try clicking on console page
                buy.click()
                time.sleep(random.randrange(2, 3))
                add_to_basket = browser.find_element_by_class_name(
                    list(data.items())[i][1]["basketClass"]).click()
                sendSuccessEmail(subject=list(data.items())[i][0] + " added to basket!!",
                                 url=list(data.items())[i][1]["url"])
                i += 1
            except:
                print(list(data.items())[i][0] + " not in stock")
                i += 1
                continue
        else:
            print(list(data.items())[i][0] +
                  " not in stock javascript:void(0)")
            i += 1
            continue

    if i == 5:
        browser.switch_to.window(browser.window_handles[i])
        browser.refresh()
        time.sleep(random.randrange(3, 4))
        anchors = browser.find_elements_by_xpath("//a")
        shopall = browser.find_element_by_xpath(
            '//a[@href="' + list(data.items())[i][1]["anchorBefore"]+'"]')
        # ps5 anchor is after the shop all anchor
        shopAllIndex = anchors.index(shopall)
        buy = anchors[shopAllIndex+1]
        if buy.get_attribute("href") != "javascript:void(0);":
            try:
                # try clicking on console page
                buy.click()
                time.sleep(random.randrange(2, 3))
                add_to_basket = browser.find_element_by_class_name(
                    list(data.items())[i][1]["basketClass"]).click()
                sendSuccessEmail(subject=list(data.items())[i][0] + " added to basket!!",
                                 url=list(data.items())[i][1]["url"])
                i += 1
            except:
                print(list(data.items())[i][0] + " not in stock")
                i += 1
                continue
        else:
            print(list(data.items())[i][0] +
                  " not in stock javascript:void(0)")
            i += 1
            continue

    if i == 6:
        browser.switch_to.window(browser.window_handles[i])
        browser.refresh()
        time.sleep(random.randrange(2, 3))
        try:
            if browser.find_element_by_id(
                    data[key]["configureButton"]).is_enabled():
                configure = browser.find_element_by_id(
                    data[key]["configureButton"]).click()
                if browser.find_element_by_xpath('//button[@role="option"]').is_enabled():
                    browser.find_element_by_xpath('//button[@role="option"]').click()
                    if browser.find_element_by_class_name(
                    'c-button').is_enabled():
                        add_to_cart = browser.find_element_by_class_name(
                    'c-button').is_enabled()
                        sendSuccessEmail(subject=key + " added to basket!!",
                                url=data[key]["url"])
                i = 0
            else:
                raise Exception('configure button not clickable')
        except:
            print(key + " not in stock")
            i = 0
            continue
