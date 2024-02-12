class Game:
    def __init__(self, xml_element):
        self.id = xml_element.get('id')
        self.path = xml_element.findtext("path")
        self.name = xml_element.findtext("name")
        self.desc = xml_element.findtext("desc")
        self.image = xml_element.findtext("image")
        self.video = xml_element.findtext("video")
        self.rating = xml_element.findtext("rating")
        self.releaseDate = xml_element.findtext("releasedate")
        self.developer = xml_element.findtext("developer")
        self.publisher = xml_element.findtext("publisher")
        self.genre = xml_element.findtext("genre")
        self.players = xml_element.findtext("players")
        self.md5 = xml_element.findtext("md5")
        self.lang = xml_element.findtext("lang")
        self.region = xml_element.findtext("region")
        self.cheevosHash = xml_element.findtext("cheevosHash")
        self.cheevosId = xml_element.findtext("cheevosId")
        self.scrap_date = xml_element.findtext("scrap_date")
        self.scrap_source = xml_element.findtext("scrap_source")

    def __str__(self):
        return f"ID: {self.id}\nName: {self.name}\nRating: {self.rating}\nGenre: {self.genre}\n"
