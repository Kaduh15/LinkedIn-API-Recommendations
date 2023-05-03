from fastapi import FastAPI

from scraping import get_Recommendations, login_linkedIn


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
        return recommendations
