import random
import pandas as pd
import os

class Plugin:
    # Define static method, so no self parameter 
    def process(self, payload):
        """
        Payload should consist of:
            - df = pandas dataframe to apply plugin to
            - veelheid = a number that states the amount of values that needs creating
        """
        df = payload['df']

        lijst_achternamen_nl = open(os.getcwd()+"/plugins/create/achternamen_value/Nederlandse_achternamen.txt").readlines()
        lijst_achternamen_nl_schoon = [achternaam_schoon.rstrip() for achternaam_schoon in lijst_achternamen_nl]

        max_achternamen = len(lijst_achternamen_nl_schoon)
        df[payload["kolomnaam"]] = [lijst_achternamen_nl_schoon[random.randrange(0, max_achternamen)] for x in range(payload["veelheid"])]
        return df