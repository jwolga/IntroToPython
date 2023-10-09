
# Создать телефонный справочник с возможностью импорта и экспорта данных в # формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи (Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

# 1. UI (user interface)
# 2. Создать файл
# 3. Читать файл
# 4. Вывод данных на экран
#     - считать файл
#     - сохранить в переменной
#     - вывести на экран
# 5. Запись контактов
#     - запросить данные
#     - сохранить в переменную
#     - записать в файл
# 6. Поиск контакта
#     - запросить данные поиска
#     - сохранить в переменную
#     - считать файл
#     - сохранить в переменную
#     - произвести поиск

def get_name():
    return input('Введите имя: ')

def get_surname():
    return input('Введите фамилию: ')

def get_patronymic_name():
    return input('Введите отчество: ')

def get_phone_number():
    return input('Введите номер телефона: ')

def get_address():
    return input('Введите адрес: ')

def create_contact():
    surname = get_surname()
    name = get_name()
    patronymic_name = get_patronymic_name()
    phone_number = get_phone_number()
    address = get_address()    
    return f'{surname} {name} {patronymic_name}\n{phone_number}\n{address}'

def add_contact():
    contact = create_contact()
    with open('PhoneBook.txt', 'a+', encoding='utf-8') as data:
        data.write(contact + '\n\n')

def read_file():
    with open('PhoneBook.txt', 'r', encoding='utf-8') as data:
        return data.read().rstrip().split('\n\n') 

def get_content(contacts):
    return '\n\n'.join(contacts)

def split_contact(contact):
    return contact.replace('\n', ' ').split()

def join_contact(parts):
    return f'{parts[0]} {parts[1]} {parts[2]}\n{parts[3]}\n{parts[4]}'

def print_contacts():
    contacts = read_file()
    print()
    print(get_content(contacts))
    return

def search_contacts(contacts, choice, search):
    search_results = []
    for contact in contacts:
        elements = split_contact(contact)
        if search.lower() in elements[choice].lower():
            search_results.append(contact)   
    return search_results

def get_search_choice(options):
    print('Варианты поиска:\n')
    options = list(enumerate(options))
    for option in options: 
        print(f'{option[0]+1}. {option[1]}')
            
    choice = input("Выберите вариант поиска: ")
    avaible_options = [str(op[0] + 1) for op in options]
    while choice not in avaible_options:
        print('Некорректный ввод')
        choice = input("Выберите вариант поиска: ")
    choice = int(choice) - 1 
    return choice   

def search_contact():
    choice = get_search_choice(('По фамилии', 'По имени','По отчеству','По номеру телефона','По адресу'))
    search = input('Введите данные для поиска: ')

    contacts = read_file()
    search_results = search_contacts(contacts, choice, search)
    if(len(search_results) == 0):
        print('Контакт не найден в справочнике')
    else:
        print('Найдены следующие контакты:')
        print(get_content(search_results))
        print()

    return search_results

'''
Домашнее задание
Дополнить телефонный справочник возможностью изменения 
и удаления данных. Пользователь также может ввести 
имя или фамилию, и Вы должны реализовать функционал для изменения
 и удаления данных.
'''
def get_contact_data(choice):
    match choice:
        case 0:
            return get_surname()
        case 1:
            return get_name()
        case 2:
            return get_patronymic_name()
        case 3:
            return get_phone_number()
        case 4:
            return get_address()

def write_file(content):     # получает содержимое файла, кот.нужно перезаписать
    with open('PhoneBook.txt', 'w', encoding='utf-8') as data:
        return data.write(content.rstrip() + '\n\n') 

def edit_contact():                # редактирование файла
    choice = get_search_choice(('По фамилии', 'По имени'))
    search = input('Введите данные для поиска: ')
    contacts = read_file()
    # поиск контакта
    search_results = search_contacts(contacts, choice, search)
    if len(search_results) == 0:
        print('Контакт не найден в справочнике')
    else:
        # запрос данных для изменения
        print('Какие данные Вы хотите изменить:\n'
              '1. Фамилия\n'
              '2. Имя\n'
              '3. Отчество\n'
              '4. Номер телефона\n'
              '5. Адрес')
        choice = input("Выберите вариант: ")
        while choice not in ('1', '2', '3', '4', '5'):
            print('Некорректный ввод')
            choice = input("Выберите вариант: ")
        choice = int(choice) - 1
        replace = get_contact_data(choice)
        # перебор результатов поиска и замена контакта
        for search_result in search_results:
            i = contacts.index(search_result)
            contact_parts = split_contact(search_result)
            contact_parts[choice] = replace
            contact = join_contact(contact_parts)
            contacts[i] = contact
        # сохранение изменений
        write_file(get_content(contacts))
        print('Данные успешно изменены\n')

def delete_contact():
    choice = get_search_choice(('По фамилии', 'По имени'))
    search = input('Введите данные для поиска: ')
    contacts = read_file()
    # поиск контакта
    search_results = search_contacts(contacts, choice, search)
    if len(search_results) != 0:
        for search_result in search_results:
            print('Вы действительно хотите удалить контакт')
            print(search_result)
            print('Да/Нет?')
            choice = input()
            if choice in ('Д', 'д', 'да', 'Да', 'ДА'):
                contacts.remove(search_result)
                # сохранение изменений
                write_file(get_content(contacts))
                print('Данные успешно удалены\n')

def user_interface():
    with open('PhoneBook.txt', 'a+', encoding='utf-8'): # создать файл если его нет
        pass
    cmd = None
    while cmd != '6':
        print('Меню: \n'
            '1. Запись контакта\n'
            '2. Вывести данные на экран\n'
            '3. Поиск контакта\n'
            '4. Изменить данные контакта\n'
            '5. Удалить данные контакта\n'
            '6. Выход')
        
        cmd = input('Введите номер операции: ')

        while cmd not in ('1', '2', '3', '4', '5', '6'):
            print('Некорректный ввод')
            cmd = input('Введите номер операции: ')
        match cmd:   # как swich 
            case '1':
                add_contact()
            case '2':
                print_contacts()
            case '3':
                search_contact()
            case '4':
                edit_contact()
            case '5':
                delete_contact()
            case '6':
                print("До скорых встреч")

user_interface()