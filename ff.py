def show_menu():
    print("Меню: add, insert, remove, check, show, exit")

shopping_list = []
command = ""

while command != "exit":
    show_menu()
    command = input("Введите команду: ")

    if command == "add":
        item = input("Введите товар: ")
        shopping_list.append(item)
        print("Товар «" + item + "» добавлен.")
        
    elif command == "insert":
        pos = int(input("Введите позицию: "))
        item = input("Введите товар: ")
        shopping_list.insert(pos, item)
        print("Товар «" + item + "» добавлен на позицию " + str(pos) + ".")
        
    elif command == "remove":
        item = input("Введите товар: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print("Товар «" + item + "» удален.")
        else:
            print("Товар «" + item + "» не найден в списке.")
            
    elif command == "check":
        item = input("Введите товар: ")
        if item in shopping_list:
            print("Товар «" + item + "» есть в списке.")
        else:
            print("Товар «" + item + "» не найден в списке.")
            
    elif command == "show":
        print("Список покупок:", shopping_list)
        
    elif command == "exit":
        print("Работа программы завершена.")
        
    else:
        print("Ошибка: неизвестная команда.")
        
    print()  # Пустая строка для разделения выводов, как в примере