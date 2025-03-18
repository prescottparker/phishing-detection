# 🚀 Phishing Detection Scraper
import requests
from bs4 import BeautifulSoup

def scan_website(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")

        # Check for phishing indicators
        if "login" in soup.text.lower() and "free" in soup.text.lower():
            return True  # Possible phishing
        return False  # Safe
    except:
        return True  # Consider non-responsive sites as phishing
