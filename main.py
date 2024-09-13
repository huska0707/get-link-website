from scraper import get_discord_link
from open_broswer import open_discord_link_in_browser
import pandas as pd


def main():
    file_path = "Spain.xlsx"
    df = pd.read_excel(file_path)

    df["Discord Link"] = None

    for index, row in df.iterrows():
        website_url = row["Website"]
        discord_link = get_discord_link(website_url)
        df.at[index, "Discord Link"] = discord_link
    # website_url = "https://walken.io/"

    output_file = "Discord_file.xlsx"
    df.to_excel(output_file, index=False)

    # open_discord_link_in_browser(discord_link)


if __name__ == "__main__":
    main()
