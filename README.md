# Fantasy Basketball Helper
Scripts to Generate Specific Stats I Need for NBA Fantasy Basketball.

## What is Fantasy Basketball?
Fantasy basketball is a game in which the participants serve as owners and general managers of virtual professional basketball teams. The competitors select their rosters by participating in a draft in which all relevant National Basketball Association (NBA) players are available. Fantasy points are awarded in weekly matchups based on the actual performances of basketball players in real-world competition <sub>[Wikipedia](https://en.wikipedia.org/wiki/Fantasy_basketball)</sub>.

## What Do I Use This Helper For?
I originally created this project because you often need to pay to see advanced stats like "quality games" on sites such as Yahoo Fantasy Basketball. My script currently only generates a version of this "quality games" advanced stat by first scraping, then parsing  regular season schedule data from [Basketball Reference](https://www.basketball-reference.com/]) using [Beautiful Soup](https://en.wikipedia.org/wiki/Beautiful_Soup_(HTML_parser)#:~:text=Beautiful%20Soup%20is%20a%20Python,is%20useful%20for%20web%20scraping.), then by locally pasting the data to a CSV file that can then be imported and manipulated with [Pandas](https://pandas.pydata.org/).

This project was also just created so I could refresh my web scraping knowledge.

In the future (probably before next season), I plan to add more advanced stats and maybe even prediction tools. I won this year 😎.
