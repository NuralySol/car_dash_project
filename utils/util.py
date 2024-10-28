import pandas as pd


# Function to load the data from the csv file and pass it to the Dash app with Path as an argument
# Return as a DataFrame and drop any missing values
def get_data(PATH):
    df = pd.read_csv(PATH)
    df.dropna(inplace=True)
    return df
