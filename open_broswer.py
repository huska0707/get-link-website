import webbrowser

def open_discord_link_in_browser(discord_link):
    if discord_link:
        print(f"Opening Discord Link: {discord_link}")
        webbrowser.open_new_tab(discord_link)
    else:
        print("No Discord Link to open")
