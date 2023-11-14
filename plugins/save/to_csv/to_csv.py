import os

class Plugin:
    # Define static method, so no self parameter 
    def process(self, payload): 
        """
        Payload should consist of:
            - df = pandas dataframe to apply plugin to
            - params: dict with one key: 
                - file_name # a string value
        """
        df = payload['df']
        params = payload['params']
        file_name = params["file_name"] if params["file_name"].endswith(".csv") else params["file_name"]+".csv"
        print(os.getcwd()+file_name)
        df.to_csv(os.getcwd()+"/"+file_name)
        return df