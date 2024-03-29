from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        dict = toml.loads(content)
        dict1 = dict["tool"]["poetry"]

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(dict1["name"], dict1["description"], dict1["license"], dict1["authors"], dict1["dependencies"], dict1["group"]["dev"]["dependencies"])
