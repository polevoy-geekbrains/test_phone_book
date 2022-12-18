from data_base import get_all_contacts
import csv

def export_csv():
    temp = get_all_contacts() # Выгрузка всей базы данных

    file_csv = "bd_csv_export.csv" # выбор файла для выгрузки

    with open(file_csv,"w", encoding='UTF-8', newline="") as file: 
        colone = temp[0].keys()
        writer = csv.DictWriter(file, fieldnames=colone)
        writer.writeheader()
        writer.writerows(temp)
    
    print(f"данные перенесены в файл {file_csv}") # перенести управление в интерфейс при подключении экспорта из других форматов

    return file_csv

