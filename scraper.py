import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Configure Chrome options (e.g., run in headless mode)
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode

def get_discord_link(website_url):
    try:

        # Start the WebDriver
        driver = webdriver.Chrome(options=chrome_options)

        driver.get(website_url)

        # Get all the anchor tags (links)
        anchors = driver.find_elements(By.TAG_NAME, 'a')

        # Regex pattern to match Discord invite links
        discord_pattern = re.compile(r"(https?://)?(www\.)?(discord\.gg|discord(app)?\.com/invite)/[a-zA-Z0-9]+")

        # Store found Discord links
        discord_links = []

        # Loop through all the anchor tags and check for Discord links
        for anchor in anchors:
            link = anchor.get_attribute('href')
            if link and discord_pattern.match(link):
                discord_links.append(link)

        # Print or use the Discord links
        print("Found Discord Links:")
        for discord_link in discord_links:
            print(discord_link)

        # Close the browser
        driver.quit()
        return discord_links

    except Exception as e:
        return [""]
