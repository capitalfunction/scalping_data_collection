

# Define function to fetch scalping data
def scalping_data(ticker, lookback_days=5):
    interval = '1m'
    end_date = dt.datetime.now()
    
    # Calculate the start date based on lookback_days
    start_date = end_date - pd.Timedelta(days=lookback_days)
    
    # Initialize an empty DataFrame to store results
    all_data = pd.DataFrame()

    # Fetch data in chunks of up to 6 days
    while start_date < end_date:
        chunk_end_date = min(start_date + pd.Timedelta(days=6), end_date)
        try:
            # Fetch data for the chunk period
            data = yf.download(ticker, start=start_date, end=chunk_end_date, interval=interval)
            data = data.reset_index()  # Reset index to have 'Datetime' as a column
            all_data = pd.concat([all_data, data], ignore_index=True)  # Append data
        except Exception as e:
            print(f"Error fetching data for {ticker} from {start_date} to {chunk_end_date}: {e}")
        
        # Move to the next chunk
        start_date = chunk_end_date

    return all_data

# Function to save data to Parquet
def save_to_parquet(data, ticker, filename):
    if not data.empty:
        # Create the folder if it doesn't exist
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        # Save or append data to a Parquet file
        if os.path.exists(filename):
            existing_data = pd.read_parquet(filename)
            # Combine new data with existing data
            combined_data = pd.concat([existing_data, data]).drop_duplicates(subset=['Datetime'])
            combined_data.to_parquet(filename, index=False)
        else:
            data.to_parquet(filename, index=False)
        print(f"Data saved to {filename}.")
    else:
        print("No new data to save.")


# Main function to run daily and update the Parquet database
def update_scalping_database(ticker, database_path='scalping_data.parquet'):
    # Load existing data to determine the last date available
    if os.path.exists(database_path):
        existing_data = pd.read_parquet(database_path)
        last_date = existing_data['Datetime'].max()
        # Calculate days since the last update
        days_since_last_update = (pd.Timestamp.now(tz='UTC').to_pydatetime() - last_date.to_pydatetime()).days # Make both datetime objects timezone aware and convert to python datetime objects
    else:
        days_since_last_update = 5  # Default to fetching the last 5 days if no data exists
    
    # Fetch new data and update the database
    new_data = scalping_data(ticker, lookback_days=days_since_last_update)
    save_to_parquet(new_data, ticker, database_path)


