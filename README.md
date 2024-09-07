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
