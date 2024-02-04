def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    with open("contacts.txt", "a") as file:
        file.write(f"{name} {phone}\n")
    return "Contact added."

def change_contact(args, contacts):
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        with open("contacts.txt", "w") as file:
            for contact_name, contact_phone in contacts.items():
                file.write(f"{contact_name} {contact_phone}\n")
        return "Contact updated."
    else:
        return "Contact not found."

def get_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return f"Phone for {name}: {contacts[name]}"
    else:
        return "Contact not found."

def show_all_contacts(contacts):
    if not contacts:
        return "No contacts available."
    else:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_phone(args, contacts))
        elif command == "all":
            print(show_all_contacts(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()