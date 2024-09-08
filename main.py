from database_operations import save_to_parquet, update_scalping_database, read_parquet_data
from data_scrape import scalping_data
from data_construction_and_preproccess.preprocess import convert_to_new_york_timezone
import logging

log_file_path = '.log'
# Configure logging
logging.basicConfig(filename='log_file_path,
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def fetch_multi_asset_1m(symbols):
    for i in symbols:
        try:
            file_dir = r'path_to_save_data'+f'{i}_scalping_data.parquet'
            data = scalping_data(ticker=i)
            save_to_parquet(data, i, file_dir)
            update_scalping_database(i, file_dir)
            logging.info(f'Successfully updated data for {i}.')
        except Exception as e:
            logging.error(f'Error for {i}: {e}')

if __name__ == "__main__":
    symbols = ['GC=F','SOL-USD','BTC-USD','ES=F','NQ=F','CL=F']
    fetch_multi_asset_1m(symbols)
    


