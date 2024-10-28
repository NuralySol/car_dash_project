import pandas as pd

def get_data(PATH):
    df = pd.read_csv(PATH)
    df.dropna(inplace=True)  
    return df