import random
import pandas as pd

class Plugin:
    # Define static method, so no self parameter 
    def process(self, payload): 
        """
        Payload should consist of:
            - veelheid = a number that states the amount of values that needs creating
            - kolomnaam = a string stating the name of the column
            - params: dict with two keys: 
                - laag # a numeric value
                - hoog # a numeric value
        """
        params = payload['params']

        return {payload['kolomnaam']: [random.randrange(params['laag'], params['hoog']) for x in range(payload['veelheid'])]}