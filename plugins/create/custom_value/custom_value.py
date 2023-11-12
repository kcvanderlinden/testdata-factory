import random

class Plugin:
    # Define static method, so no self parameter 
    def process(self, payload): 
        """
        Payload should consist of:
            - df = pandas dataframe to apply plugin to
            - veelheid = a number that states the amount of values that needs creating
            - kolomnaam = a string stating the name of the column
            - params: dict with one keys: 
                - list_custom_values # a list containing any values
                - hoog # a numeric value
        """
        df = payload['df']
        params = payload['params']

        max_aangepaste_lijst = len(params["list_custom_values"])
        df[payload["kolomnaam"]] = [params["list_custom_values"][random.randrange(0, max_aangepaste_lijst)] for x in range(payload['veelheid'])]
        return df 