import pandas as pd
import os

# Function to save data to Parquet
def save_to_parquet(data, ticker, filename):
    if not data.empty:
        # Ensure the 'Datetime' column is set as the index for efficient deduplication
        if 'Datetime' not in data.index.names:
            data = data.set_index('Datetime')

        # Create the folder if it doesn't exist
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        # Save or append data to a Parquet file
        if os.path.exists(filename):
            # Load existing data
            existing_data = pd.read_parquet(filename)

            # Ensure the 'Datetime' column is set as the index for the existing data as well
            if 'Datetime' not in existing_data.index.names:
                existing_data = existing_data.set_index('Datetime')

            # Combine new data with existing data and remove duplicates based on the index
            combined_data = pd.concat([existing_data, data]).loc[~pd.concat([existing_data, data]).index.duplicated(keep='last')]

            # Save combined data to Parquet
            combined_data.to_parquet(filename)
        else:
            # Save new data to a Parquet file
            data.to_parquet(filename)

        print(f"Data saved to {filename}.")
    else:
        print("No new data to save.")


# Main function to run daily and update the Parquet database
def update_scalping_database(ticker, database_path='scalping_data.parquet'):
    # Load existing data to determine the last date available
    if os.path.exists(database_path):
        existing_data = pd.read_parquet(database_path)

        # Check if 'Datetime' column exists. If not, try 'Date'
        if 'Datetime' in existing_data.columns:
            last_date = existing_data['Datetime'].max()
        elif 'Date' in existing_data.columns:
            last_date = existing_data['Date'].max()
        else:
            # Handle case where neither column exists
            print("Error: No 'Datetime' or 'Date' column found in the Parquet file.")
            return

        # Calculate days since the last update
        days_since_last_update = (pd.Timestamp.now(tz='UTC').to_pydatetime() - last_date.to_pydatetime()).days # Make both datetime objects timezone aware and convert to python datetime objects
    else:
        days_since_last_update = 5  # Default to fetching the last 5 days if no data exists

    # Fetch new data and update the database
    new_data = scalping_data(ticker, lookback_days=days_since_last_update)
    save_to_parquet(new_data, ticker, database_path)



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
