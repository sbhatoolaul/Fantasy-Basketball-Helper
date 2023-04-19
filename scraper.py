import requests
# from time import sleep
# import random
from bs4 import BeautifulSoup
import pandas as pd

def scrape_regular_season_schedule():
    # Fetch Current data for 2022-23 NBA Season
    data = []

    # URLs = [
    #     "https://www.basketball-reference.com/leagues/NBA_2023_games-october.html",
    #     "https://www.basketball-reference.com/leagues/NBA_2023_games-november.html",
    #     "https://www.basketball-reference.com/leagues/NBA_2023_games-december.html",
    #     "https://www.basketball-reference.com/leagues/NBA_2023_games-january.html",
    #     "https://www.basketball-reference.com/leagues/NBA_2023_games-february.html",
    #     "https://www.basketball-reference.com/leagues/NBA_2023_games-march.html",
    #     "https://www.basketball-reference.com/leagues/NBA_2023_games-april.html",
    # ]
    # Right now, we are just using a local copy of each HTMl site to avoid an IP ban
    URLs = [
        "./data/local-saves/NBA_2023-games-october.html",
        "./data/local-saves/NBA_2023-games-november.html",
        "./data/local-saves/NBA_2023-games-december.html",
        "./data/local-saves/NBA_2023-games-january.html",
        "./data/local-saves/NBA_2023-games-february.html",
        "./data/local-saves/NBA_2023-games-march.html",
        "./data/local-saves/NBA_2023-games-april.html",
    ]

    for URL in URLs:
        # Again, we are currently just using a local copy of each HTMl site instead to avoid an IP ban
        # But, this is how we would do it normally:
        # file = requests.get(URL)
        # In the real version, we would also sleep between requests to further imitate a real user--we could also use proxies
        # sleep(random.randint(5, 16))
        # Then, we would continue parsing with BeautifulSoup as normal...

        with open(URL) as file:
            soup = BeautifulSoup(file, 'html.parser')

            table = soup.find('table', id="schedule").find('tbody')
            rows = table.find_all('tr')
            for row in rows:
                date = row.find_all('th')[0].text.strip()
                if date == 'Tue, Apr 11, 2023': # first non-regular season game of 2023
                    break

                #      date     rest of info
                info = [date] + [element.text.strip() for element in row.find_all('td')]

                data.append(info)

    df = pd.DataFrame(data, columns=["Date", "Start(ET)", "Visitors", "PTS", "Home", "PTS", "", "", "In Attendance", "Arena", "Notes"])

    df.to_csv("./data/2022-2023 NBA Regular Season Schedule.csv", index=False)