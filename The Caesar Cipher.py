while True:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    alphabeteng = "abcdefghijklmnopqrstuvwxyz"
    # выбор команды
    n = int(input("Выберите команду\n1.Зашифровать сообщение\n2.Расшифровать сообщение\n3.Выход из программы\n")) - 1
    # выход из программы
    if n == 2:
        quit("Вы вышли из программы")
    # ввод сообщения для шифрования/расшифровки
    message = input("Введите сообщение для шифрования русскими буквами: ") if not n else input("Введите"
                                                                                               " строку для расшифровки"
                                                                                               " русскими буквами: ")
    # проверка сообщения на английские символы
    for letter in message:
        if letter in alphabeteng:
            quit("Ошибка\nВ вашем сообшении возможно находятся английские буквы!\nПерезапустите программу")
    key = int(input("Введите ключ: "))
    key = key if not n else -1 * key
    message1 = ""
    # шифрование/расшифровка сообщения
    for letter in message:
        position = alphabet.find(letter)
        newPosition = position + key
        if letter in alphabet:
            message1 = message1 + alphabet[newPosition]
        else:
            message1 = message1 + letter
    print("Зашифрованное сообщение: ", message1) if not n else print("Расшифрованное сообщение: ", message1)
