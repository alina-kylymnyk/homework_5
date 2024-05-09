commands_list = [
    " enter 'close', 'exit' - to stop the bot",
    " enter 'hello', - to enter the command",
    " enter 'phone <name>' - to get the phone of the contact",
    " enter 'add <name> <phone number>' - to add new contact",
    " enter 'all' - to see all the contacts"
]


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Not enough arguments provided."
        except KeyError as e:
            return f"Error: {e} not found."
        except Exception as e:
            return f"An unexpected error occurred: {e}. Please try again."

    return inner


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise ValueError
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return f"Contact information for {name} updated."
    else:
        raise KeyError


@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        raise ValueError
    name = args[0]
    if name in contacts:
        return f"The phone number for {name} is: {contacts[name]}"
    else:
        raise KeyError


@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts available."
    all_contacts = "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    return f"All contacts:\n{all_contacts}"


@input_error
def main():
    contacts = {
        'Den': "092837489",
        'Steve': "2038475",
        'Bob': "84478392"
    }

    print("Welcome to the assistant bot! Write 'help' to see what I can do or enter a command.")
    while True:
        user_input = input("Enter a command: ").strip().lower()
        if not user_input:
            continue
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "help":
            for line in commands_list:
                print(line)
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        else:
            print("Invalid command. Type 'help' for instructions.")


if __name__ == "__main__":
    main()
