import pandas as pd
import yfinance as yf
import datetime as dt
from dateutil.relativedelta import relativedelta

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
            # print(all_data)
        except Exception as e:
            print(f"Error fetching data for {ticker} from {start_date} to {chunk_end_date}: {e}")

        # Move to the next chunk
        start_date = chunk_end_date
        # Set 'Datetime' column as index and convert to DatetimeIndex
        all_data = all_data.set_index('Datetime')
        all_data.index = pd.to_datetime(all_data.index)



    return all_data
