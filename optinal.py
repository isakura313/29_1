def get_full_name(name, otchesvo, surname):
    """ Вариативно возращает данные о пользователе """
    if otchesvo:
        full_name = name.strip().title() + " " + otchesvo.strip().title() + " " + surname.strip().title()
    else:
        full_name = name.strip().title() + " " + surname.strip().title()
    return full_name


name = input("Введите имя: ")
otchestvo = input("Введите отчество: ")
surname = input("Введите фамилию: ")

print(get_full_name(name, otchestvo, surname))

