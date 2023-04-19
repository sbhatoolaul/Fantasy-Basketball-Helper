import pandas as pd
from scraper import scrape_regular_season_schedule

class Helper:
    def __init__(self):
        pass

    def get_quality_games(self):
        # scrape_regular_season_schedule()  # do not need to run this multiple times if running local
        df = pd.read_csv('./data/2022-2023 NBA Regular Season Schedule.csv')

        days = {}
        for index, row in df.iterrows():
            day = row['Date']
            team1 = row['Visitors']
            team2 = row['Home']

            if day not in days:
                days[day] = set()
            days[day].add(team1)
            days[day].add(team2)


        teams = {}
        for day in days:
            for team in days[day]:
                if team not in teams:
                    teams[team] = []
                teams[team].append(len(days[day]))

        data = []
        for team in teams:
            data.append([team, sum(teams[team])/82])

        quality = pd.DataFrame(data, columns=["Teams", "Avg # of Teams Playing Same Night"])
        quality.sort_values("Avg # of Teams Playing Same Night", inplace=True)
        quality = quality.reset_index(drop=True)

        print(quality)

if __name__ == '__main__':
    Helper().get_quality_games()
