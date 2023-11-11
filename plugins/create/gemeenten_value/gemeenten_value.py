import random
import pandas as pd

class Plugin:
    # Define static method, so no self parameter 
    def process(self, veelheid):
        gemeenten_wiki = pd.read_csv("./Nederlandse_gemeenten.txt", sep=" \t", header=None)
        gemeenten_namen = gemeenten_wiki[0].to_list()

        max_gemeenten = len(gemeenten_namen)
        return {"Gemeente": [gemeenten_namen[random.randrange(0, max_gemeenten)] for x in range(veelheid)]}