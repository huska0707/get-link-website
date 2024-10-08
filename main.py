from scraper import get_discord_link
from open_broswer import open_discord_link_in_browser
import pandas as pd
from tqdm import tqdm
import time

def main():
    file_path = "canada.xlsx"  # file name
    df = pd.read_excel(file_path)

    cnt_url = len(df)
    discord_column_name = "Discord-Links"
    if discord_column_name not in df.columns:
        df[discord_column_name] = ""  # or you can initialize with np.nan or any default value
    for i in tqdm(range(cnt_url)):
        try:
            print(df.iloc[i]["Website"])
            website_url = df.iloc[i]["Website"]
            discord_urls = get_discord_link(website_url)
            n_urls = []
            for url in discord_urls:
                if url not in n_urls:
                    n_urls.append(url)
            print(n_urls)
            df.at[i, discord_column_name] = ", ".join(n_urls)
        except Exception as e:
            print(e)
    df.to_excel("canada-Discord.xlsx")

if __name__ == "__main__":
    main()






    
