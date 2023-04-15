from fastapi import FastAPI

from scraping import get_Recommendations, login_linkedIn, URL_BASE
from driver import DRIVER


is_login = login_linkedIn()

app = None

if is_login:
    app = FastAPI()

    @app.get("/")
    def read_root():
        return {"Hello": "World"}

    @app.get("/username/{username}")
    def get_recommendations(username: str):
        recommendations = get_Recommendations(username)
        DRIVER.get(URL_BASE)
        return recommendations
