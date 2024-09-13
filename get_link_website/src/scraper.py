import requests
from bs4 import BeautifulSoup


def get_discord_link(website_url):
    try:
        response = requests.get(website_url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            link = soup.find_all("a", href=True)

    except Exception as e:
        return f"Error occured: {str(e)}"
