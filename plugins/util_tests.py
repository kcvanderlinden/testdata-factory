import pandas as pd

def create_standard_dataframe(custom_data: dict = None) -> pd.DataFrame:
    # Create a dictionary of data
    data = {
        'id': [1,2,3,4],
        'Name': ['Alice', 'Bob', None, 'David'],
        'Age': [25, None, 35, 28],
        'City': ['New York', 'San Francisco', None, 'Chicago'],
        'Gender': ['Female', None, 'Male', 'Male'],
        'Salary': [60000, None, 80000, 55000],
        'Cool': [True, False, None, True]
    } if custom_data is None else custom_data

    return pd.DataFrame(data)

def create_merge_dataframe(custom_data: dict = None) -> pd.DataFrame:
    data = {
        'id': [1,2,3,4],
        'Surname': ['Carter', 'Marley', 'Steijn', 'Hasselhoff'],
    } if custom_data is None else custom_data

    return pd.DataFrame(data)