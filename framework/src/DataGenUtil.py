import os
import json

def list_of_dict_to_csv(list_of_dict, includeHeaders = True):
    csv_str = ''
    if includeHeaders == True:
        header = []
        for column_name in list_of_dict[0].keys(): 
            if not column_name.startswith('_'): header.append(column_name)
        csv_str += ",".join(header) + "\n"

    for row in list_of_dict:
        csv_str += obj_to_csv(row) + "\n"

    return csv_str

def obj_to_csv(obj):
    csv = ''
    for key in obj:
        if not (key.startswith('_')): csv += str(obj[key]) + ','
    return csv[:-1]

def list_of_dict_to_json(list_of_dict):
    json_str = '['
    for row in list_of_dict:
        json_str += obj_to_json(row) + ",\n"
    return json_str[:-2] + ']'

def obj_to_json(obj):
    json_dict = {}
    for key in obj:
        if not (key.startswith('_')): json_dict[key] = obj[key]
    return json.dumps(json_dict)

class FileWriter:
    def __init__(self, root_destination=None):
        if not root_destination: self.root_destination = ''
        elif not root_destination.endswith('/'): self.root_destination = root_destination + '/'
        else: self.root_destination = root_destination
        self.writers = {}

    def write(self, path_and_filename, data_str):
        path_and_filename = self.root_destination + path_and_filename
        if path_and_filename not in self.writers.keys():
            if not os.path.exists(os.path.dirname(path_and_filename)):
                os.makedirs(os.path.dirname(path_and_filename))
            self.writers[path_and_filename] = open(path_and_filename, 'a')
        
        self.writers[path_and_filename].write(data_str)    