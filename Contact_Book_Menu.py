contacts = {}
items = []

while True:
    selection = int(input("1 add, 2 search, 3 list, 0 quit: "))
    if selection == 1:
        name = input("Name: ")
        phone = input("Phone: ")
        if name not in contacts:
            contacts[name] = []
        contacts[name].append(phone)
    elif selection == 2:
        name = input("Name: ")
        print(contacts.get(name, "Not Found"))
    elif selection == 3:
        for names in sorted(contacts):
            print(names, ", ".join(contacts[names]))
    elif selection == 0:
        break

