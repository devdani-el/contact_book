contacts = []

def add_contact():
    while True:
        print('Enter "exit" to stop.')
        name = str(input('Name: ')).strip().capitalize()
        if name.lower() == 'exit':
            break
        number = int(input('Tel: '))

        novo_contato = {'name': name, 'number': number}
        contacts.append(novo_contato)


while True:
    print('CONTACT BOOK 📒')
    print('-' * 30)
    for contact in contacts:
        print(f"Name: {contact['name']} \nPhone number: {contact['number']}\n")
    print('Enter 1: + new contact')
    menu = int(input('Option: '))
    if menu == 1:
        add_contact()
    print('-' * 30)
