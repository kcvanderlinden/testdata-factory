import random
import pandas as pd

class Plugin:
    # Define static method, so no self parameter 
    def process(self, veelheid):
        lijst_achternamen_nl = open("./Nederlandse_achternamen.txt").readlines()
        lijst_achternamen_nl_schoon = [achternaam_schoon.rstrip() for achternaam_schoon in lijst_achternamen_nl]

        max_achternamen = len(lijst_achternamen_nl_schoon)
        return {"Achternaam": [lijst_achternamen_nl_schoon[random.randrange(0, max_achternamen)] for x in range(veelheid)]}