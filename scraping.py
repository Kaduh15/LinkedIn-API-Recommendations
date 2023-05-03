import os
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv, find_dotenv
from selenium import webdriver

load_dotenv(find_dotenv())

URL_BASE = "https://www.linkedin.com"
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

options = webdriver.chrome.options.Options()
if os.getenv('ENV') != "development":
    options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-setuid-sandbox")
options.add_argument("--disable-extensions")


service = ChromeService(executable_path=ChromeDriverManager().install())
DRIVER = webdriver.Chrome(options=options, service=service)


def login_linkedIn():
    login_url = URL_BASE + "/login"
    DRIVER.get(login_url)
    sleep(3)

    input_email = DRIVER.find_element(By.XPATH, '//*[@id="username"]')
    input_password = DRIVER.find_element(By.XPATH, '//*[@id="password"]')
    btn_login = DRIVER.find_element(
        By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')

    input_email.send_keys(EMAIL)
    input_password.send_keys(PASSWORD)
    btn_login.click()

    print('Login successful!')

    return True


def get_Recommendations(username: str):
    DRIVER.get(f'{URL_BASE}/in/{username}/details/recommendations')
    sleep(15)

    recommendations_recieved = DRIVER.find_element(
        By.XPATH,
        "/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section/div[2]/div[2]/div/div/div[1]/ul",
    )

    lis = recommendations_recieved.find_elements(
        By.CSS_SELECTOR, "li.pvs-list__paged-list-item"
    )

    formatted_recommendations = []

    for li in lis:
        formatted_recommendations.append(format_recommendations(li))

    return formatted_recommendations


def get_img_url(li: WebElement):
    img = li.find_element(By.CSS_SELECTOR, 'img')
    return img.get_attribute('src')


def get_name(li: WebElement):
    name = li.find_element(
        By.CSS_SELECTOR, 'a > div > span > span.visually-hidden')
    return name.text


def get_title(li: WebElement):
    description = li.find_element(
        By.CSS_SELECTOR, 'a > span > span.visually-hidden')
    return description.text


def get_recommended(li: WebElement):
    recommended = li.find_element(
        By.CSS_SELECTOR,
        'li.pvs-list__item--with-top-padding'
    )
    return recommended.text


def format_recommendations(li: WebElement):
    return {
        "img_url": get_img_url(li),
        "name": get_name(li),
        "title": get_title(li),
        "recommended_text": get_recommended(li)
    }


if __name__ == "__main__":
    login_linkedIn()
    # recommendations = get_Recommendations('kaduh15')
    # print(recommendations)
