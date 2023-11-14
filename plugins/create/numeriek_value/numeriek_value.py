import random

class Plugin:
    # Define static method, so no self parameter 
    def process(self, payload): 
        """
        Payload should consist of:
            - df = pandas dataframe to apply plugin to
            - veelheid = a number that states the amount of values that needs creating
            - kolomnaam = a string stating the name of the column
            - params: dict with two keys: 
                - laag # a numeric value
                - hoog # a numeric value
        """
        df = payload['df']
        params = payload['params']
        df[payload["kolomnaam"]] = [random.randrange(params['laag'], params['hoog']+1) for x in range(payload['veelheid'])]
        return df