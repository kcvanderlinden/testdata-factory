import random
import pandas as pd
import os

class Plugin:
    # Define static method, so no self parameter 
    def process(self, payload):
        """
        Payload should consist of:
            - df = pandas dataframe to apply plugin to
            - kolomnaam = a string stating the name of the column
            - veelheid = a number that states the amount of values that needs creating
        """
        df = payload['df']
        gemeenten_wiki = pd.read_csv(os.getcwd()+"/plugins/create/gemeenten_value/Nederlandse_gemeenten.txt", sep=" \t", header=None)
        gemeenten_namen = gemeenten_wiki[0].to_list()

        max_gemeenten = len(gemeenten_namen)
        df[payload["kolomnaam"]] = [gemeenten_namen[random.randrange(0, max_gemeenten)] for x in range(payload["veelheid"])]
        return df