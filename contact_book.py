from os import system, name


contacts = []

def add_contact():
    while True:
        print('Add a new contact 📘')
        print('Enter "exit" to stop.')
        name = str(input('Name: ')).strip().capitalize()
        if name.lower() == 'exit':
            break

        while True:
            try:
                number = int(input('Number: '))
                break
            except ValueError:
                print('Please enter a valid number.')

        while True:
            email = input('E-mail: ').strip().lower()
            if email == '':
                clear_screen()
                break
            elif email == 'no':
                break
            if '@' not in email or '.' not in email:
                print('Please enter a valid email.')
            else:
                clear_screen()
                break

        new_contact = {'name': name, 'number': number, 'email': email}
        contacts.append(new_contact)


def search_contact():
    message = str(input('Contact to search: ')).capitalize().strip()
    found = False
    for contact in contacts:
        if message == contact['name']:
            print(f"Name: {contact['name']}\nPhone number: {contact['number']}\nE-mail address: {contact['email']}")
            found = True
            break
    if not found:
        print("Contact not found.")

def clear_screen():
    system('cls' if name == 'nt' else 'clear')


while True:
    clear_screen()
    print('CONTACT BOOK 📒')
    print('-' * 30)
    for contact in contacts:
        print(f"Name: {contact['name']} \nPhone number: {contact['number']} \nE-mail address: {contact['email']}\n")
    print('Enter 1: + new contact')
    print('Enter 2: Search a contact')
    try:
        menu = int(input('Option: '))
        if menu == 1:
            clear_screen()
            add_contact()
        elif menu == 2:
            clear_screen()
            search_contact()
        print('-' * 30)
    except ValueError:
        print('Please enter a valid option.')
