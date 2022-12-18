import csv
import json

def import_csv(path_to_import_csv_file): 
    ''' Управление импортом из файла import_phonebook.csv'''

    data = []      
    with open(path_to_import_csv_file, "r", newline='', encoding='UTF-8-sig') as file: 
        file_reader = csv.DictReader(file, delimiter = ";") 
        for row in file_reader:
            data.append(row)     
        for i in range(0, len(data)): 
            d1 = {'contact_id': ''}
            data[i], d1 = d1, data[i]
            data[i].update(d1)     

    return data 
    
def import_json(path_to_import_json_file):
    ''' Управление импортом из файла import_phonebook.json'''

    data = []   
    with open(path_to_import_json_file, 'r', encoding='UTF-8') as file:
        data = json.load(file) 
        for i in range(0, len(data)): 
            d1 = {'contact_id': ''}
            data[i], d1 = d1, data[i]
            data[i].update(d1)
    return data

