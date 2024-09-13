import requests
from bs4 import BeautifulSoup
import re


def get_discord_link(website_url):
    try:
        response = requests.get(website_url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            print("soup:", soup)
            links = soup.find_all("a", href=True)

            discord_pattern = re.compile(r"(https://discord\.(gg|com/invite)/[^\s]+)")

            for link in links:
                if discord_pattern.match(link["href"]):
                    return link["href"]
        return None

    except Exception as e:
        return f"Error occured: {str(e)}"
