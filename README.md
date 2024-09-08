**Scalping Data Pipeline**


**Objective:**
- There is a data restriction on yfinance to download 1m data. 
- In order for Machine Learning algorithms to aviod overfitting, the least that can be done is have more data.
- To build up a database with 


This project involves scraping financial data at a one-minute interval for multiple assets, storing the data in Parquet format, and updating the stored data daily. The data scraping and storage process is broken down into three Python scripts:

- `data_scrape.py`: Fetches one-minute interval data from Yahoo Finance for a specified ticker.
- `database_operations.py`: Contains functions to save scraped data to Parquet files and update the database with new data.
- `main.py`: The main script that orchestrates the data scraping and saving operations, handles multiple assets, and maintains logs for tracking.

## 1. File Descriptions

### data_scrape.py

This script fetches historical data at a one-minute interval for a given ticker from Yahoo Finance.

### **Key Functions:**

- **`scalping_data(ticker, lookback_days=5)`**:
    - Parameters:
        - `ticker` (str): The ticker symbol of the asset (e.g., 'BTC-USD', 'AAPL').
        - `lookback_days` (int): Number of days to look back from the current date to fetch data (default is 5 days).
    - Returns: A DataFrame containing the asset's historical data at a one-minute interval.
    - Process:
        1. Calculates the start and end dates for data fetching based on the current date and `lookback_days`.
        2. Uses the `yfinance` library to download data in chunks of up to 6 days at a time (to avoid API limits).
        3. Concatenates each fetched chunk of data into a single DataFrame.
        4. Returns the consolidated DataFrame with the `Datetime` column set as the index.

### database_operations.py

This script contains functions to handle data storage and database updates using the Parquet file format.

### **Key Functions:**

- **`save_to_parquet(data, ticker, filename)`**:
    - Parameters:
        - `data` (DataFrame): The data to be saved.
        - `ticker` (str): The ticker symbol of the asset.
        - `filename` (str): The path to the Parquet file.
    - Process:
        1. Checks if the data is not empty.
        2. Sets the `Datetime` column as the index for efficient deduplication.
        3. Creates the directory if it doesn't exist.
        4. If the file exists, loads existing data, concatenates it with new data, removes duplicates, and saves it back. If the file doesn't exist, saves new data directly.
        5. Prints a message confirming the save operation.
- **`update_scalping_database(ticker, database_path='scalping_data.parquet')`**:
    - Parameters:
        - `ticker` (str): The ticker symbol of the asset.
        - `database_path` (str): The path to the Parquet database file.
    - Process:
        1. Loads existing data to determine the last available date.
        2. Calculates the days since the last update.
        3. Fetches new data for the missing period using the `scalping_data` function.
        4. Saves the new data using the `save_to_parquet` function.
- **`read_parquet_data(filename)`**:
    - Parameters:
        - `filename` (str): The path to the Parquet file.
    - Returns: A DataFrame loaded from the specified Parquet file.
    - Process:
        1. Tries to read data from a Parquet file and returns the DataFrame.
        2. If an error occurs, it prints an error message and returns an empty DataFrame.

### main.py

The main script to manage the entire process of scraping and saving data for multiple assets.

### **Key Functions and Process:**

- **Logging Configuration**:
    - Sets up a logging configuration to log messages to a specified log file.
- **`fetch_multi_asset_1m(symbols)`**:
    - Parameters:
        - `symbols` (list): A list of ticker symbols to fetch data for.
    - Process:
        1. Iterates over the list of symbols.
        2. Calls `scalping_data` to fetch data.
        3. Calls `save_to_parquet` to save the data.
        4. Calls `update_scalping_database` to update the database.
        5. Logs successful updates or errors.
- **Main Execution Block**:
    - Defines a list of symbols (e.g., `['GC=F', 'SOL-USD', 'BTC-USD', 'ES=F', 'NQ=F', 'CL=F']`).
    - Calls `fetch_multi_asset_1m(symbols)` to process the data for all symbols.

## 2. Instructions for Setting Up Daily Automation

To automate the execution of `main.py` daily, you can use the following methods for Windows:


### Windows: Using Task Scheduler

Step 1: Run Command Prompt as Administrator
Press Win + S to open the search bar.
Type cmd.
Right-click on Command Prompt and select Run as administrator.
This will open the Command Prompt with administrative privileges. You should see Administrator: Command Prompt in the window title.

Step 2: Ensure Correct Permissions and Path
Ensure the .bat file is located in a directory that does not have restrictive permissions. If needed, move the .bat file to a simpler path like C:\scripts\run_fetch_data_daily.bat.
Make sure the paths in your script and .bat file are accessible and have the necessary read/write permissions.
Step 3: Run the schtasks Command with Correct Parameters
Now, re-run the schtasks command with administrative privileges:

bash

schtasks /create /tn "FetchDataDaily" /tr "C:\scripts\run_fetch_data_daily.bat" /sc daily /st 09:00 /rl highest /ru SYSTEM

Explanation of the modified parameters:

/rl highest: Run with the highest privileges.
/ru SYSTEM: Runs the task under the SYSTEM account, which has higher privileges and does not require a password. This is often used when running tasks that need elevated permissions.

Step 4: Verify Task Creation
After executing the command, you should see a confirmation message that the task has been successfully created. To verify:

bash

schtasks /query /tn "FetchDataDaily"

Step 5: Test the Task
To test the scheduled task, run:

bash
schtasks /run /tn "FetchDataDaily"

Step 6: Ensure Proper Permissions on Python Installation
Ensure that the Python executable path used in your .bat file also has proper permissions and is accessible by the SYSTEM or administrator account.

Final Check
If you still face issues, make sure:

Your user account has administrative privileges.
The Task Scheduler service is running.
The task is created with the correct paths and syntax.

## 3. Requirements

Make sure to have the following Python libraries installed:

- `pandas`
- `yfinance`
- `pyarrow` (for Parquet support)
- 'fastparquet'
- 'os'
  


**### 4. Logging**

## Logs are stored in a log file specified in `main.py`. Ensure that the path is correctly set and accessible.

**### 5. Troubleshooting**
### Steps
- Ensure that Python and all required libraries are properly installed.
- Verify that file paths and folder permissions are correctly set.
- If there are any errors, check the log file for detailed error messages.


