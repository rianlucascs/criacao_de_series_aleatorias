
from numpy.random import uniform
from random import randint

def generate_input_numbers(range_static_numbers=[-100, 100],
                           range_index_dynamic_numbers=[1, 10],
                           range_dynamic_number=[-100, 100]):

    static_number_m = uniform(range_static_numbers[0], range_static_numbers[1])
    static_number_s = uniform(range_static_numbers[0], range_static_numbers[1])
                
    number_of_dynamic_numbers = randint(range_index_dynamic_numbers[0], range_index_dynamic_numbers[1])

    dynamic_number_a = [uniform(range_dynamic_number[0], range_dynamic_number[1]) for _ in range(number_of_dynamic_numbers)]

    return [static_number_m,
            static_number_s,
            number_of_dynamic_numbers,
            dynamic_number_a]