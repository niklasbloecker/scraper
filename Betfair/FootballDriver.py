from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import threading
import requests

BASE_URL = "https://www.betfair.com"


def getSource(link):
    print("getSource call received.")

    PATH = "../Driver/chromedriver89"
    option = webdriver.ChromeOptions()

    # Removes navigator.webdriver flag

    # For older ChromeDriver under version 79.0.3945.16
    option.add_experimental_option("excludeSwitches", ["enable-automation"])
    option.add_experimental_option("useAutomationExtension", False)

    # For ChromeDriver version 79.0.3945.16 or over
    option.add_argument("--disable-blink-features=AutomationControlled")

    # Open Browser
    browser = webdriver.Chrome(executable_path=PATH, options=option)
    browser.get(BASE_URL + link)
    element = (
        WebDriverWait(browser, 10)
        .until(EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler")))
        .click()
    )

    return browser.page_source


def matchOdds(list):
    print("matchOdds call received.")
    # TODO Multithreading für die beiden Methoden
    for game in list:
        t1 = threading.Thread(target=gameOdds, args=(game,))
        t1.start()
    print(threading.activeCount())


def gameOdds(link):
    soup = bs(requests.get(BASE_URL + link).content, features="html5lib")
    odds = soup.select('div[class*="-MATCH_ODDS-"]')
    if len(odds) > 0:
        elementList = odds[0].findAll("li")
        print(
            elementList[0].get_text().replace("\n", ""),
            " ",
            elementList[1].get_text().replace("\n", ""),
            " ",
            elementList[2].get_text().replace("\n", ""),
        )
