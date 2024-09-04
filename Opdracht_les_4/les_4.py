games = [
    "Player’s Unknown Battle Ground (PUBG) 50 Million 2018",
    "Fortnite Battle Royale 39 Million 2017",
    "Apex Legends 50 Million (1 Month) 2019",
    "Leauge of Legends (LOL) 27 Million 2009",
    "Counter Strike; Global Offensive 32 Million 2014",
    "Heartstone 29 Million 20120",
    "Minecraft 91 Million 2011",
    "DOTA 2 5 million 2015",
    "The Division 2 N/A 2019",
    "The Splatoon 2",
]
print(games)
print(games[4])

print(f"Er zitten {len(games)} games in de lijst.")

games.insert(1, "Snake Games")
print(games)

removed_game = games[games.index("The Splatoon 2")]
print(f"Helaas heeft de game {removed_game} het niet gered om in de top 10 te blijven. We nemen waardig afscheid van {removed_game}.")
games.remove(removed_game)
print(games)

change_text = games.index("Heartstone 29 Million 20120")
games[change_text] = "Heartstone 29 Million 2012"
print(games)