def is_strong(password):
    return len(password) >= 8

password = input("Введите пароль: ")
print("Надёжный пароль!" if is_strong(password) else "Слабый пароль!")