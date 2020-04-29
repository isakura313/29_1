persons = {'names':[], 'surnames': []}


def add_person(name, surname):
    """ Возвращает словарь с информацией о человеке"""
    persons['names'].append(name.strip().title())
    persons['surnames'].append(surname.strip().title())
    return persons

user_amount = int(input("Сколько пользователей? "))

for user in range(user_amount):
    name = input("Введите имя пользователя: ")
    surname = input("Введите фамилию пользователя: ")
    add_person(name, surname)


print(persons)