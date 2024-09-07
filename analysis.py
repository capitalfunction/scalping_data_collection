import pandas as pd

# Function to read data from a Parquet file
def read_parquet_data(filename):
    try:
        # Read data from the Parquet file
        data = pd.read_parquet(filename)
        print(f"Data loaded successfully from {filename}.")
        return data
    except Exception as e:
        print(f"Error reading data from {filename}: {e}")
        return pd.DataFrame()  # Return an empty DataFrame if reading fails
