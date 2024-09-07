# scalping_data_collection

# Scalping Data Fetcher and Storage in Parquet Format

This project provides a Python-based solution for fetching high-frequency (1-minute interval) stock data using the `yfinance` library and storing it efficiently in Parquet format for scalping strategies or other high-frequency trading (HFT) needs. The script is designed to handle data limitations with the `yfinance` library, fetch data efficiently, store it in a database, and update the data daily.

## Features

- **Fetch High-Frequency Data:** Fetch 1-minute interval data for up to 6 days due to `yfinance` limitations and handle fetching efficiently in chunks.
- **Data Storage in Parquet Format:** Store the fetched data in Parquet format, a highly efficient file format for large datasets, ensuring data integrity and reducing storage space.
- **Automated Daily Updates:** Automatically update the stored data daily to keep the database relevant, even if the script is not run for a few days.
- **Robust Error Handling:** Provides error handling for API requests, missing data, and file operations.
- **Easy Data Retrieval and Analysis:** Load data from the Parquet database and perform operations such as filtering, technical analysis, and visualization.

## Requirements

- Python 3.7 or later
- Required Python libraries:
  - `yfinance`
  - `pandas`
  - `pyarrow` (for reading/writing Parquet files)
  - `matplotlib` (for visualization)

Install the required libraries using pip:

```bash
pip install yfinance pandas pyarrow matplotlib parquet

**## Project Structure**
.
├── data/
│   └── AAPL_scalping_data.parquet  # Example output file (Parquet format)
├── scalping_data.py                # Main script for fetching and updating data
├── analysis.py                     # Script for retrieving and analyzing data
└── README.md                       # Project documentation

Usage
1. Fetch and Store Scalping Data
The scalping_data.py script is the core component of the project. It fetches 1-minute interval data for a given stock ticker and stores it in Parquet format.

Example Usage
To update the scalping data for a specific stock (e.g., AAPL), run the update_scalping_database function:
# Example: Fetch and update data for AAPL
from scalping_data import update_scalping_database

update_scalping_database('AAPL', 'data/AAPL_scalping_data.parquet')
This will:

- Check the last date in the existing Parquet file.
- Fetch new data from that date to the current date.
- Append the new data to the Parquet file, ensuring no duplicates.

2. Retrieve and Analyze Data
Use the analysis.py script to load the Parquet data and perform various analyses, such as filtering by date, calculating moving averages, or visualizing the data.

Example Usage
Load the data and display a summary:
from analysis import read_parquet_data

# Load data from Parquet file
data = read_parquet_data('data/AAPL_scalping_data.parquet')

# Display first few rows and a summary
print(data.head())
print(data.describe())

3. Automating Daily Updates
To ensure that your Parquet database remains up-to-date, you can automate the script execution using a task scheduler:

Windows: Use Task Scheduler to run the Python script daily.
Linux/macOS: Use a cron job to run the script daily. Example cron job entry:

0 0 * * * /usr/bin/python3 /path/to/scalping_data.py


Contributing
Contributions are welcome! If you have any ideas or improvements, feel free to submit a pull request or open an issue.



This doesnt include data Visualization steps.

To-Do:
 Add support for multiple tickers in a single run.
 Integrate with other data sources for more comprehensive datasets.
 Implement additional technical indicators and trading strategies.

Acknowledgments
yfinance for providing an easy-to-use API for fetching financial data.
pandas for powerful data manipulation and analysis.
pyarrow for efficient data storage in Parquet format.
matplotlib for data visualization capabilities. 
