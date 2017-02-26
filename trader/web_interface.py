from selenium import webdriver
from elementium.drivers.se import SeElements

class WebInterface():

    def __init__(self):
        self.se = SeElements(webdriver.Chrome())
        self.se.navigate("https://www.predictit.org/Browse/Featured")

    def getMarketList(self):
        self.market_list = self.se.find("#marketList").find("#row").find(".a")
        print(len(self.market_list))