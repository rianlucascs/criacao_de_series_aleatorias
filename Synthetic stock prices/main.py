
from utils.synthetic_data_generator import synthetic_data_generator
from utils.generate_input_numbers import generate_input_numbers
from utils.utils import add_path, generate_random_key, complex_writing
from utils.scans_folders import scans_folders
from os import listdir

def __init__(ticker, number_of_days, quantity_of_inputs_numbers, quantity_of_series_generated):
    
    folder_ticker = ticker.upper().split('.')[0]
    folder_number_of_days = str(number_of_days)

    _ = scans_folders(folder_ticker, folder_number_of_days)

    list_input_numbers = [generate_input_numbers() for _ in range(quantity_of_inputs_numbers)]
    amount_of_existing_inputs = len(listdir(add_path(['data', folder_ticker, folder_number_of_days, 'inputs_numbers'])))
    for file, input_numbers in enumerate(list_input_numbers):
        file += amount_of_existing_inputs
        if file == quantity_of_inputs_numbers:
            break

        path_inputs_numbers = add_path(['data', folder_ticker, folder_number_of_days, 'inputs_numbers', f'{file}.txt'])
        complex_writing(path_inputs_numbers, str(input_numbers))

        static_number_m, static_number_s, number_of_dynamic_numbers, dynamic_number_a = input_numbers
        for _ in range(quantity_of_series_generated):
            path_output_series = add_path(['data', folder_ticker, folder_number_of_days, 'outputs_series', f'{file}_{generate_random_key(32)}.txt'])
            synthetic_data = synthetic_data_generator(ticker, number_of_days, static_number_m, static_number_s, dynamic_number_a)
            complex_writing(path_output_series, str(synthetic_data))

        print(f'{file} / {amount_of_existing_inputs + quantity_of_inputs_numbers - 1}')

__init__('vale3.sa', 1500, 20, 10)