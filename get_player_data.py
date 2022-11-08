from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

class Player():
    def __init__(self, name):
        self.name = name
        self.teams = {}
        self.positions = None
        self.bats = None
        self.throws = None
        self.career_stats = {}
        self.accolades = []
        self.numbers = []
        self.birth_place = None

def get_player_data(link):

    html = urlopen(link)
    bsObj = BeautifulSoup(html.read(),features="lxml")

    # Preform a BS find function to get the position of our player
    player_name = bsObj.find("h1").get_text().strip()

    my_player = Player(name = player_name)

    player_data = bsObj.findAll("p")

    for data in player_data:
        bio_info = data.find("strong")

        if bio_info:
            if bio_info.get_text().strip() == "Position:" or bio_info.get_text().strip() == "Positions:":
                my_player.positions = data.get_text().split("\n")[2].lstrip()

            if bio_info.get_text().strip() == "Bats:":
                my_player.bats = data.get_text().split("\n")[1].split(" ")[1]
                my_player.throws = data.get_text().replace("\t","").split("\n")[3].split(" ")[1]

            if bio_info.get_text().strip() == "Born:":
                my_player.birth_place = data.get_text().split("\n")[7].lstrip().replace("in ","")


    career_stats = bsObj.find("div", {"class": "p1"}).findAll("div")

    for stat in career_stats:

        name = stat.find("strong").get_text()
        try:
            value = stat.findAll("p")[1].get_text()
        except:
            value = stat.findAll("p")[0].get_text()

        my_player.career_stats[name] = value

    career_stats = bsObj.find("div", {"class": "p3"}).findAll("div")

    for stat in career_stats:
        name = stat.find("strong").get_text()

        try:
            value = stat.findAll("p")[1].get_text()
        except:
            value = stat.findAll("p")[0].get_text()

        my_player.career_stats[name] = value

    accolades = bsObj.find("ul", {"id": "bling"})\

    if accolades:
        accolades = accolades.findAll("li")

        for accolade in accolades:
            my_player.accolades.append(accolade.get_text())

    numbers = bsObj.find("div", {"class": "uni_holder br"}).findAll("a")

    for number in numbers:
        number = number.find("text").get_text()

        if number not in my_player.numbers:
            my_player.numbers.append(number)


    data_table = bsObj.find("table", {"id": "batting_standard"})

    team_images = {}

    for row in data_table.findAll(lambda tag: tag.name == 'tr' and (tag.get('class') == ['full'] or tag.get('class') == ['partial_table'])):

        year = row.find("th").get_text()

        try:
            team = row.find("a").get_text()
            team_link = "https://www.baseball-reference.com" + row.find("a")['href']
        except:
            continue


        if team == 'AL' or team == 'NL' or len(team) != 3:
            continue

        elif team in my_player.teams.keys():
            my_player.teams[team].append(year)

        else:
            my_player.teams[team] = [year]
            team_images[team] = team_link

    for team, link in team_images.items():
        html = urlopen(link)
        bsImg = BeautifulSoup(html.read(), features="lxml")

        player_image_url = bsImg.find("img", {"class":"teamlogo"})['src']
        urlretrieve(player_image_url, f"manim_images/{team}.jpg")

    return my_player

