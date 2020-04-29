def titling(name = "Аноним", surname= "Анонимов"):
    print(name.strip().title() + " " + surname.strip().title())


name_if_user = input("введите ваше имя: ")
surname_of_user = input("Введите вашу фамилию: ")
titling(surname = surname_of_user, name = name_if_user)
titling()