import random
import string

def generate_password(length=12, use_digits=True, use_symbols=True, use_uppercase=True):
    if length < 4:
        raise ValueError("Password too short")

    # Категорії символів
    lowercase = list(string.ascii_lowercase)
    digits = list(string.digits) if use_digits else []
    symbols = list("!@#$%^&*()-_=+") if use_symbols else []
    uppercase = list(string.ascii_uppercase) if use_uppercase else []

    # Формуємо загальний набір вибраних символів
    all_chars = lowercase + digits + symbols + uppercase
    if not all_chars:
        raise ValueError("No characters selected for password generation")

    # Гарантуємо наявність хоча б одного символу з кожної вибраної категорії
    password_chars = []
    password_chars.append(random.choice(lowercase))  # завжди є маленькі літери

    if digits:
        password_chars.append(random.choice(digits))
    if symbols:
        password_chars.append(random.choice(symbols))
    if uppercase:
        password_chars.append(random.choice(uppercase))

    # Заповнюємо решту пароля випадковими символами з усього набору
    remaining_length = length - len(password_chars)
    password_chars += random.choices(all_chars, k=remaining_length)

    # Перемішуємо, щоб гарантійні символи були розподілені випадково
    random.shuffle(password_chars)

    return ''.join(password_chars)
