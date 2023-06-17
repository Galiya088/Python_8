def add_contact():
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    phone_number = input("Введите номер телефона: ")

    with open("справочник.txt", "a") as file:
        file.write(f"{surname},{name},{phone_number}\n")

    print("Контакт успешно добавлен!")


def search_contacts():
    search_key = input("Введите фамилию или имя для поиска: ")
    found_contacts = []

    with open("справочник.txt", "r") as file:
        for line in file:
            surname, name, phone_number = line.strip().split(",")
            if (
                search_key.lower() in surname.lower()
                or search_key.lower() in name.lower()
               
            ):
                found_contacts.append((surname, name, phone_number))

    if found_contacts:
        print("Результаты поиска:")
        for contact in found_contacts:
            print(f"Фамилия: {contact[0]}, Имя: {contact[1]}, Номер телефона: {contact[2]}")
    else:
        print("Контакты не найдены.")


def import_contacts():
    filename = input("Введите имя файла для импорта: ")
    try:
        with open(filename, "r") as file:
            contacts = [line.strip().split(",") for line in file]
        
        with open("справочник.txt", "a") as file:
            for contact in contacts:
                file.write(",".join(contact) + "\n")

        print("Контакты успешно импортированы!")
    except FileNotFoundError:
        print("Файл не найден.")


def export_contacts():
    filename = input("Введите имя файла для экспорта: ")
    contacts = []

    with open("справочник.txt", "r") as file:
        for line in file:
            contacts.append(line.strip().split(","))

    with open(filename, "w") as file:
        for contact in contacts:
            file.write(",".join(contact) + "\n")

    print("Контакты успешно экспортированы!")


def update_contact():
    search_key = input("Введите фамилию или имя контакта для обновления: ")
    updated_contacts = []

    with open("справочник.txt", "r") as file:
        for line in file:
            surname, name, phone_number = line.strip().split(",")
            if (
                search_key.lower() in surname.lower()
                or search_key.lower() in name.lower()
            ):
                print(f"Найден контакт: Фамилия: {surname}, Имя: {name}, Номер телефона: {phone_number}")
                new_surname = input("Введите новую фамилию (оставьте пустым, чтобы оставить прежнее значение): ")
                new_name = input("Введите новое имя (оставьте пустым, чтобы оставить прежнее значение): ")
                
                new_phone_number = input("Введите новый номер телефона (оставьте пустым, чтобы оставить прежнее значение): ")

                if not new_surname:
                    new_surname = surname

                if not new_name:
                    new_name = name
                
                if not new_phone_number:
                    new_phone_number = phone_number

                updated_contacts.append((new_surname, new_name, new_phone_number))
            else:
                updated_contacts.append((surname, name, phone_number))

    with open("справочник.txt", "w") as file:
        for contact in updated_contacts:
            file.write(",".join(contact) + "\n")

    print("Контакт успешно обновлен!")


def delete_contact():
    search_key = input("Введите фамилию или имя контакта для удаления: ")
    deleted_contacts = []

    with open("справочник.txt", "r") as file:
        for line in file:
            surname, name, phone_number = line.strip().split(",")
            if (
                search_key.lower() in surname.lower()
                or search_key.lower() in name.lower()
            ):
                print(f"Удален контакт: Фамилия: {surname}, Имя: {name}, Номер телефона: {phone_number}")
            else:
                deleted_contacts.append((surname, name, phone_number))

    with open("справочник.txt", "w") as file:
        for contact in deleted_contacts:
            file.write(",".join(contact) + "\n")

    print("Контакт успешно удален!")


while True:
    print("\nТелефонный справочник")
    print("1. Добавить контакт")
    print("2. Поиск контактов")
    print("3. Импорт контактов")
    print("4. Экспорт контактов")
    print("5. Обновить контакт")
    print("6. Удалить контакт")
    print("7. Выйти")

    choice = input("Выберите действие: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contacts()
    elif choice == "3":
        import_contacts()
    elif choice == "4":
        export_contacts()
    elif choice == "5":
        update_contact()
    elif choice == "6":
        delete_contact()
    elif choice == "7":
        break
    else:
        print("Неверный выбор. Попробуйте снова.")


