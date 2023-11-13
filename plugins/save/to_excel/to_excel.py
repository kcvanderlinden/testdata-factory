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
        file_name = params["file_name"] if params["file_name"].endswith(".xlsx") else params["file_name"]+".xlsx"
        print(os.getcwd()+file_name)
        df.to_excel(os.getcwd()+"/"+file_name)
        return df