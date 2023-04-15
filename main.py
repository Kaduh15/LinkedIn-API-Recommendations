from fastapi import FastAPI

from scraping import get_Recommendations

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/username/{username}")
def get_recommendations(username: str):
    recommendations = get_Recommendations(username)
    return recommendations
