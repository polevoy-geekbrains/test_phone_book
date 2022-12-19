import time

def error_input():
    '''вывод ошибки'''

    print('Будьте внимательны! Что-то пошло не так!')
    print('Введите соответствующую команду!')
    time.sleep(1)

def done_message():
    print('Выполнено!\n')

main_menu = \
    'Выберите пункт меню:\n\
    1. Поиск контакта\n\
    2. Добавить контакт\n\
    3. Редактировать контакт\n\
    4. Импорт контактов\n\
    5. Экспорт контактов\n\
    6. Телефонная книга\n\
    7. Выход'

def start_page(): 
    '''вывод гллавного меню'''

    print(main_menu)
    print()
    command = input('Выберите действие: ')
    return command

def search_contact():
    ''' поиск контакта'''

    search_request = input('Введите данные для поиска: ')
    print(50 * "=")
    return search_request

def add_contact():
    '''добавление контакта'''

    print('Добавление контакта: ')
    print(50 * "-")
    contact_surname = input('Введите фамилию: ')  
    contact_name = input('Введите имя: ')  
    contact_number = input('Введите номер телефона: ')
    commentary = input('Введите комментарий: ')
    contact = [{'contact_id': '', 'surname': contact_surname, 'name': contact_name, 'phone': contact_number,
                'comment': commentary}, ]
    return contact 

def change_contact():

    ''' ввлд контакта для редактирования или удаления'''

    print('Изменить контакт: ')
    print(50 * "~")
    contact_id = input('Выберите контакт для внесения изменений: ')
    return int(contact_id)

def change_contact_content(one_contact):

    ''' редактирование контакта'''

    while True:
        menu_command = input('Что необходимо сделать?\n 1 - Редактировать контакт \n 2 - Удалить контакт\n')
        if menu_command == '1':
            print('Редактирование контакта:')
            while True:
                submenu_command = input(
                    'Что необходимо изменить?\n 1 - Изменить фамилию \n 2 - Изменить имя\n 3 - Изменить номер телефона\n 4 - Изменить комментарий\n')
                match submenu_command:
                    case '1':  # Изменить фамилию
                        print('Введите фамилию: ')
                        one_contact['surname'] = input()
                        done_message()
                        break
                    case '2':  # Изменить имя
                        print('Введите имя: ')
                        one_contact['name'] = input()
                        done_message()
                        break
                    case '3':  # Изменить номер телефона
                        print('Введите номер телефона: ')
                        one_contact['phone'] = input()
                        done_message()
                        break
                    case '4':  # Изменить комментарий
                        print('Введите комментарий: ')
                        one_contact['comment'] = input()
                        done_message()
                        break
                    case _:
                        error_input()
            break
        elif menu_command == '2':
            one_contact['comment'] = 'Я что-то нажал и всё сломалось'  # удаление по ID
            done_message()
            break
    return one_contact
   
def bye_mess():
    print('Работа закончена!')

def import_contacts():

    '''импорт контактов из файла'''

    print('Импорт контактов: ')
    print('Выберите формат файла для импорта: ')
    import_type = input('1. import_phonebook.csv\n2. import_phonebook.json\n')
    return import_type

def export_contacts():

    '''экспорт котактов в файл'''

    print('Экспорт контактов: ')
    print('Выыберите формат файла для экпорта: ')
    export_type = input('csv\njson\n')
    return export_type

def show_contacts(data):  

    '''вывод в консоль всего списка контактов'''
    
    if data != []:
        print(50 * "*")
        print('Список всех контактов: ')
        for item in range(len(data)):
            a = data[item]['contact_id']
            b = data[item]['surname']
            c = data[item]['name']
            d = data[item]['phone']
            e = data[item]['comment']
            print(f'{a}) {b} {c}. {d}. {e}.')
    else:
        print('Список контактов пуст')

def result_mess(done):
    if done:
        done_message()
    else:
        print('При выполнении операции произошла ошибка!')

def result_import(name_file):
    print(f'Контакты успешно импортированы из {name_file}.\n')