from scraper import get_discord_link
from open_broswer import open_discord_link_in_browser
import pandas as pd


def main():
    file_path = "Spain.xlsx"
    df = pd.read_excel(file_path)
    print(df.columns)
    websites = df["Website"]

    for website in websites:
        print(website)
    # website_url = "https://uptopsearch.com/"
    # discord_link = get_discord_link(website_url)

    # open_discord_link_in_browser(discord_link)


if __name__ == "__main__":
    main()
