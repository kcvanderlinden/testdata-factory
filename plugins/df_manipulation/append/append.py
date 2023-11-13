import pandas as pd

class Plugin:
    # Define static method, so no self parameter 
    def process(self, payload):
        """
        Payload should consist of:
            - df_from_steps = a list containing the dataframe that should be appended
        """
        df = pd.concat(payload["params"], ignore_index=True)

        return df