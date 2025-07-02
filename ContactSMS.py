import time


def log_dec(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"ketgan vaqti: {end - start} ")

    return wrapper


class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def get_info(self):
        return f" Ism: {self.name}   Telefon raqami: {self.phone}"


class ContactManager:
    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.contacts = []

    def get_owner_info(self):
        return f"Kontakt menejeri: {self.owner_name}"

    def show_all_contacts(self):
        if not self.contacts:
            print(" Kontaktlar yo‘q")
        else:
            print("                    |Kontaktlar ro‘yxati|")
            for i, c in enumerate(self.contacts, 1):
                print(f"{i}. {c.get_info()}")

    def get_all_phones(self):
        return [c.phone for c in self.contacts]

    @log_dec
    def add_contact(self, name, phone):
        contact = Contact(name, phone)
        self.contacts.append(contact)
        print(f"Kontakt qo‘shildi: {name}")

    def add_ready_contact(self, contact_obj):
        self.contacts.append(contact_obj)

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"{name} o‘chirildi")
                return
        print(f" {name} topilmadi")

class SMSManager:
    def __init__(self, contact_manager):
        self.contact_manager = contact_manager
        self.sent_sms = []

    def send_sms(self, phone, message):
        if not self.is_valid_phone(phone):
            print(" Telefon raqam formati noto‘g‘ri!")
            return

        if phone not in self.contact_manager.get_all_phones():
            print("Bu raqam kontaktlar ro‘yxatida yo‘q!")
            return

        self.sent_sms.append((phone, message))
        print(f" SMS yuborildi → {phone}")
        print(f"Yuborilgan  Xabar: {message}")

    def is_valid_phone(self, phone):
        return phone.startswith("+998") and len(phone) == 13 and phone[1:].isdigit()


manager = ContactManager("Mansurbek")
sms = SMSManager(manager)

a1 = Contact("ali ", '+998942873399')
a2 = Contact("avaz akam ", '+998939561703')
a3 = Contact("rixsitilla ", '+998500059343')
a4 = Contact("anvar akam  ", '+998943040615')
a5 = Contact("mansurbek ", '+998940463606')
a6 = Contact("mansurbek2 ", '+998770008824')
a7 = Contact("javohir", '+998931973325')
a8 = Contact("Malika", "+998933335555")
a9 = Contact("Jasur", "+998991112233")
a10 = Contact("Sevara", "+998909988877")

manager.add_ready_contact(a1)
manager.add_ready_contact(a2)
manager.add_ready_contact(a3)
manager.add_ready_contact(a4)
manager.add_ready_contact(a5)
manager.add_ready_contact(a6)
manager.add_ready_contact(a7)
manager.add_ready_contact(a8)
manager.add_ready_contact(a9)
manager.add_ready_contact(a10)


while True:
    print("                               |Asosiy bo‘lim:|")
    b= input( '1-Kontankt menjer  | 2-SMS menejer  | 0-dasturdan chiqish | >>> Tanlang: ')
    if b == '1':
        while True:
            print("                                                   | Kontakt Menejeri |")
            a = input('1-Barcha kontaktlar | 2-Kontakt qo‘shish | 3-Kontakt o‘chirish | 4-orqaga qaytish : ')
            if a== '1':
                manager.show_all_contacts()
            elif a == '2':
                ism = input("Ism: ")
                tel = input("Telefon (+998XXXXXXXXX): ")
                manager.add_contact(ism, tel)
            elif a == '3':
                ism = input("O‘chirish uchun ism: ")
                manager.delete_contact(ism)
            elif a == '4':
                break
            else:
                print("Noto‘g‘ri tanlov!")

    elif b == '2':
        phone = input(" Telefon raqami (+998XXXXXXXXX): ")
        msg = input("  Xabar matni: ")
        sms.send_sms(phone, msg)

    elif b == '0':
        print("`Dasturdan chiqildi.")
        break
    else:
        print(" Siz adashdingiz, qaytadan urinib koring!")

