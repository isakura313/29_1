def titling(name = "Аноним", surname= "Анонимов"):
    full_name = (name.strip().title() + " " + surname.strip().title())
    return full_name


name_if_user = input("введите ваше имя: ")
surname_of_user = input("Введите вашу фамилию: ")
FULL_NAME = titling(surname = surname_of_user, name = name_if_user)
print(FULL_NAME)
titling()