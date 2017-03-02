from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from elementium.drivers.se import SeElements
import time


class WebInterface():

    YES = 1
    NO = 0

    def __init__(self, user, pwd):
        self.se = SeElements(webdriver.Chrome())
        self.se.navigate("https://www.predictit.org/Account/SignIn")

        b = None
        while not b:
            b = self.se.find("button[type='submit']")
            time.sleep(0.5)
        self.se.find("input[type='email']").write(user)
        self.se.find("input[type='password']").write(pwd)
        try:
            b.click()
        except Exception:
            pass

    def make_trade(self, contract, option, quantity, max_price):
        self.se.navigate("https://www.predictit.org/Contract/"+str(contract))

        for b in self.se.find("button"):
            if option == self.YES and b.text() == "Buy Yes":
                b.click()
            elif option == self.NO and b.text() == "Buy No":
                b.click()

        i = None
        while not i:
            i = self.se.find("input[id='Quantity']")
            time.sleep(0.5)
        i.write(Keys.BACK_SPACE)
        i.write(str(quantity))
        i = None
        while not i:
            i = self.se.find("input[id='PricePerShare']")
            time.sleep(0.5)
        i.write(Keys.BACK_SPACE + Keys.BACK_SPACE)
        i.write(str(max_price))
        for b in self.se.find("button"):
            if b.text() == "Preview":
                b.click()
        for b in self.se.find("button"):
            if b.text() == "Submit Offer":
                b.click()
