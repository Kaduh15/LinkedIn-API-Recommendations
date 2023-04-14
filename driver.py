import os
from selenium import webdriver
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

URL_BASE = "https://www.linkedin.com"

opts = webdriver.ChromeOptions()
opts.add_argument("--window-size=710,1000")
if os.getenv('ENV') == "production":
    opts.add_argument("--headless")

DRIVER = webdriver.Chrome(options=opts)
DRIVER.get(URL_BASE)
