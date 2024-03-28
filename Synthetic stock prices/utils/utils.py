from os import path, name, sep
from os import mkdir, getcwd, remove
from secrets import token_hex
import json

def get_funcion_name():
    from inspect import currentframe, getouterframes
    frame = currentframe()
    function_name = getouterframes(frame)[1].function
    return function_name

def get_operating_system_name():
    systems = {'nt': 'windows', 'posix': 'mac'}
    if name not in systems.keys():
        raise SystemError(f'*Erro {get_funcion_name()}')    
    else:
        return systems[name]
    
def detect_folder_separator():
    _system_name = get_operating_system_name()
    if _system_name == 'windows':
        row_sep = len(sep)
        match row_sep:
            case 0:
                raise SystemError(f'*Erro {get_funcion_name()}')
            case 1:
                _sep = sep
                __sep = _sep + _sep
            case 2:
                _sep = sep[0]
                __sep = sep
        return _sep, __sep, row_sep
    elif _system_name == 'mac':
        return '/', '/', 1
    
def get_path_folder():
    _system_name = get_operating_system_name()
    _separator = detect_folder_separator()
    current_path = getcwd()
    match _system_name:
        case 'windows':
            return current_path.replace(_separator[0], _separator[1]) + _separator[1]
        case 'mac':
            return current_path + _separator[0]
        
def add_path(list_archives=[], bar_last=False):
    _path_folder = get_path_folder()
    _separator = detect_folder_separator()
    for i, archive in enumerate(list_archives):
        _path_folder += archive
        if i != len(list_archives) - 1:
            _path_folder += _separator[1]
    if bar_last:
        _path_folder += _separator[1]
    return _path_folder

def detect_path(_path):
    if path.exists(_path):
        return True
    return False

def create_folder(_path):
    if not detect_path(_path):
        mkdir(_path)
    return None

def generate_random_key(length):
    return token_hex(length//2)

def get_encoding():
    _system_name = get_operating_system_name()
    match _system_name:
        case 'windows':
            return 'UTF-8'
        case 'mac':
            return 'ISO-8859-15'
        
def simple_writing(_path, message):
    _encoding = get_encoding()
    with open(_path, 'a', encoding=_encoding) as archive:
        archive.write(message)
    return None

def complex_writing(_path, message, update=False, skip_the_line=False, skip_execution=False):
    if skip_execution:
        return None
    if update:
        if detect_path(_path):
            remove(_path)
    if skip_the_line:
        message = message + '\n'
    simple_writing(_path, message)
    return None

def complex_reading(_path, type):
    types = {'read': lambda arquivo: arquivo.read(), 
             'readlines': lambda arquivo: arquivo.readlines(),
             'json': lambda arquivo: json.load(arquivo)}
    _encoding = get_encoding()
    with open(_path, 'r', encoding=_encoding) as archive:
        if type in types:
            return types[type](archive)
        
