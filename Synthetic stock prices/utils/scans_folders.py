
from utils.utils import create_folder, add_path

def scans_folders(folder_ticker, folder_number_of_days):
    
    create_folder(add_path(['data', folder_ticker,]))
    create_folder(add_path(['data', folder_ticker, folder_number_of_days]))
    create_folder(add_path(['data', folder_ticker, folder_number_of_days, 'inputs_numbers']))
    create_folder(add_path(['data', folder_ticker, folder_number_of_days, 'outputs_series']))

    return None