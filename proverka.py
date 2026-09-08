def make_phone(raw):
    try:
        # Приводим к строке
        text = str(raw)
        
        # Проверяем, что все символы — цифры
        if not text.isdigit():
            return None
        
        # Проверяем длину (не больше 11 цифр)
        if len(text) > 11:
            return None
        
        # Если всё ок — добавляем + и возвращаем
        number = "+" + text
        return number
        
    except Exception as e:
        print(f"ошибка: {e}")
        return None
        
    finally:
        print("проверка номера завершена")


# Тесты
print(make_phone("79995553435"))   # +79995553435
print(make_phone("123"))           # +123
print(make_phone("123456789012"))  # None (12 цифр > 11)
print(make_phone("7999a553435"))   # None (есть буква)
print(make_phone(79995553435))     # +79995553435 (работает с int)
print(make_phone("+79995553435"))  # None (есть +)