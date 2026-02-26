from collections import UserDict

class Field:                   # Базовий клас для полів запису.
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):             # Клас для зберігання імені контакту. Обов'язкове поле.
    # реалізація класу
		pass

		
class Phone(Field):            # Клас для зберігання номера телефону. Має валідацію формату (10 цифр).
    def __init__(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Please insert 10 numbers")
        super().__init__(value) # з логіки прописаного батьківського Field - по суті ми маємо повернути туди поле
    
class Record:                  # Клас для зберігання інформації про контакт, включно з іменем та списком телефонів.
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        phone = Phone(phone_number)     # Створюю об'єкт Phone з phone_number
        self.phones.append(phone)       # Додаю його в список self.phones  
               
    def remove_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:  # Порівнюю значення (а не об'єкт)
                self.phones.remove(phone)
                break                            
    
    def edit_phone(self, old_number, new_number):
         for phone in self.phones:
            if phone.value == old_number:  
                phone.value = new_number
                break  

    def find_phone(self, phone_number):
       for phone in self.phones:
            if phone.value == phone_number:
                return phone  # Повертаємо об'єкт Phone
            return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):   # Клас для зберігання записів та керування ними
    def add_record ():             # додає запис до self.data
    def find():                    # знаходить запис за ім'ям
    def delete():                  # видаляє запис за ім'ям
