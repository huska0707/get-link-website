from scraper import get_discord_link

def main():
    website_url = "https://uptopsearch.com/"
    discord_link = get_discord_link(website_url)

    print(discord_link)

if __name__ == "__main__":
    main()
