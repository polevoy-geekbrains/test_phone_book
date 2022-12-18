import interface
import data_base
import logger
import import_file as iff
import export_file


def run():
    '''Запуск и обработка главного меню'''
    
    while True:
    
        command = interface.start_page()

        match command:
            
            case '1':
                '''Пункт 1 поиск контакта'''

                user_search = interface.search_contact()
                data = data_base.get_contact_info(user_search)
                interface.show_contacts(data)
            
            
            case '2':
                '''Пункт 2 добавление контакта'''

                new_contact = interface.add_contact()
                data_base.add_contacts(new_contact)
                logger.add(new_contact, 'added')
                interface.done_message()

            case '3':
                '''Пункт 3 изменение или удаление контакта'''

                data = data_base.get_all_contacts()
                interface.show_contacts(data)
                deal_id = interface.change_contact()
                one_contact = data_base.get_one_contact(deal_id)
                changed_contact = interface.change_contact_content(one_contact)
                if changed_contact['comment'] == 'Я что-то нажал и всё сломалось':
                    data_base.delete_contact(changed_contact['contact_id'])
                    logger.add(changed_contact, 'deleted')
                else:
                    data_base.change_contact(changed_contact)
                    logger.add(changed_contact, 'changed')
            
            case '4':
                '''Пункт 4 импорт контактов из файла'''

                user_choice = interface.import_contacts()
                if user_choice == '1':
                    data = iff.import_csv('import_phonebook.csv')
                    data_base.add_contacts(data)
                    interface.result_mess(True)
                    interface.result_import('import_phonebook.csv')
                    logger.add(data, 'imported')
                elif user_choice == '2':
                    data = iff.import_json('import_phonebook.json')
                    data_base.add_contacts(data)
                    interface.result_mess(True)
                    interface.result_import('import_phonebook.json')
                    logger.add(data, 'imported')
                else:
                    interface.error_input()
                
                
            
            case '5':
                '''Пункт 5 экспорт котактов в файл'''
                
                export_file.export_csv()
                
            case '6':
                '''Пункт 6 вывод в консоль всего списка контактов'''

                data = data_base.get_all_contacts()
                interface.show_contacts(data)
            
            case '7':
                '''Пункт 7 выход из программы'''

                interface.bye_mess()
                break
            
            case _:
                interface.error_input()

