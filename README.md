# Генератор паролів (Flask API)

Простий API для генерації випадкових паролів із заданими параметрами.

## Встановлення

1. Клонувати репозиторій або розпакувати ZIP.
2. Створити віртуальне середовище:
   ```bash
   python -m venv venv
   source venv/bin/activate  # або venv\\Scripts\\activate на Windows
3. Встановити залежності:
   ```bash
   pip install -r requirements.txt

## Запуск застосунку
   ```bash
   python run.py
   ```

API буде доступне за адресою:
http://127.0.0.1:5000/generate-password

## Приклади API-запитів

POST /generate-password
- Генерує пароль на основі параметрів.

Body JSON може містити такі поля:

| Поле           | Тип     | Обов'язкове | За замовчуванням | Опис                            |
|----------------|---------|-------------|------------------|---------------------------------|
| `length`       | int     | ні          | 12               | Довжина пароля (мін. 4)         |
| `use_digits`   | boolean | ні          | true             | Включати цифри                  |
| `use_symbols`  | boolean | ні          | true             | Включати спецсимволи (!@#$...)  |
| `use_uppercase`| boolean | ні          | true             | Включати великі літери          |


Приклад запиту (cURL)
   ```
   curl -X POST http://127.0.0.1:5000/generate-password \
     -H "Content-Type: application/json" \
     -d '{"length": 16, "use_digits": true, "use_symbols": true, "use_uppercase": false}'
```
Приклад відповіді
```
{
  "password": "qd!mr29d8zv4awhj"
}
```
