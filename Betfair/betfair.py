from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs
import FootballDriver


PATH = "../Driver/chromedriver89"
BASE_URL = "https://www.betfair.com"

option = webdriver.ChromeOptions()


# Removes navigator.webdriver flag

# For older ChromeDriver under version 79.0.3945.16
option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_experimental_option("useAutomationExtension", False)

# For ChromeDriver version 79.0.3945.16 or over
option.add_argument("--disable-blink-features=AutomationControlled")


# Open Browser
browser = webdriver.Chrome(executable_path=PATH, options=option)
browser.get(BASE_URL + "/sport/inplay")
element = (
    WebDriverWait(browser, 10)
    .until(EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler")))
    .click()
)
example_list = browser.find_elements_by_class_name("details-event")

sports_list = {}
sports_list["football"] = []
sports_list["tennis"] = []
sports_list["basketball"] = []
sports_list["table-tennis"] = []
sports_list["handball"] = []
sports_list["ice-hockey"] = []
sports_list["baseball"] = []
sports_list["volleyball"] = []
sports_list["badminton"] = []
sports_list["rugby-union"] = []


for link in example_list:
    source = link.get_attribute("innerHTML")
    soup = bs(source, "html.parser")
    link = soup.a["href"]
    link_split = link.split("/")
    sports_list[link_split[2]].append(link)
browser.quit()

FootballDriver.matchOdds(sports_list["football"])

# print(sports_list["football"])
