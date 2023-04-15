import os
from selenium.webdriver import Chrome, ChromeOptions
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

URL_BASE = "https://www.linkedin.com"


def set_chrome_options() -> ChromeOptions:
    """Sets chrome options for Selenium.
    Chrome options for headless browser is enabled.
    """
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--window-size=710,1000")
    if os.getenv('ENV') == "production":
        chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_prefs = {}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    return chrome_options


DRIVER = Chrome(options=set_chrome_options())
DRIVER.get(URL_BASE)
