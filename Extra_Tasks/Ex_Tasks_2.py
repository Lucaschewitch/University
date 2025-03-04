def add_contact(phone_book: dict) -> dict:
  name = input("Введите имя контакта:")
  phone = input("Введите номер телефона:")
  standartized_name = standartize_name(name)
  standartized_phone = standartize_phone(phone)
  new_phone_book = phone_book.copy()
  new_phone_book[standartized_name] = standartized_phone
  print("Контакт успешно добавлен!")
  return new_phone_book


def delete_contact(phone_book: dict) -> dict:
  name = input("Введите имя контакта:")
  standartized_name = standartize_name(name)
  if standartized_name in phone_book:
    new_phone_book = phone_book.copy()
    del new_phone_book[standartized_name]
    print("Контакт удален!")
    return new_phone_book
  else:
    print("Контакт не найден!")
    return phone_book

def view_contact(phone_book: dict) -> dict:
  if not phone_book:
    print("Телефонная книга пуста!")
  else:
    for name, phone in phone_book.items():
      print(f"{name}: {phone}")

def edit_contact(phone_book: dict) -> dict:
  name = input("Введите имя контакта:")
  standartized_name = standartize_name(name)

  if standartized_name in phone_book:
    phone = input("Введите номер телефона:")
    standartized_phone = standartize_phone(phone)
    new_phone_book = phone_book.copy()
    new_phone_book[standartized_name] = standartized_phone
    print("Номер телефона успешно изменен!")
    return new_phone_book
  else:
    print("Контакт не наден!")
    return phone_book

def standartize_name(name: str) -> str:

  return name.title()


def standartize_phone(phone: str) -> str:
  phone_digits = ''.join(char for char in phone if char.isdigit())
  if len(phone_digits) == 10:
    return "+7" + phone_digits
  elif len(phone_digits) == 11:
    return "+7" + phone_digits[1:]

  return phone_digits

def menu() -> None:
  phone_book = {}
  while True:
    print("Выберите функцию:\n", "1. Создать контакт", "2. Удалить контакт",
        "3. Показать список контактов", "4. Изменить номер", "5. Выход\n", sep="\n")
    print()

    choice = input("Введите номер функции: ")
    if choice == '1':
      phone_book = add_contact(phone_book)
      print()
    elif choice == '2':
      phone_book = delete_contact(phone_book)
      print()
    elif choice == '3':
      view_contact(phone_book)
      print()
    elif choice == '4':
      phone_book = edit_contact(phone_book)
      print()
    elif choice == '5':
      print("Выход из программы")
      break
    else:
      print("Неверный выбор! Попробуйте снова.")

menu()