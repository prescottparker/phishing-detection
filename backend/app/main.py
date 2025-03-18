# 🚀 Backend Server (FastAPI)
from fastapi import FastAPI
from app.scraper import scan_website

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Phishing Detection API"}

@app.get("/scan/")
def scan(url: str):
    result = scan_website(url)
    return {"url": url, "is_phishing": result}
