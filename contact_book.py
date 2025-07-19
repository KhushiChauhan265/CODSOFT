import os
import time

def slow_print(msg):
    for ch in msg:
        print(ch, end='', flush=True)
        time.sleep(0.015)
    print()

CONTACTS_FILE = "contacts.txt"#contact file

# Load contacts from file into a list of dictionaries
def load_contacts():
    contacts = []
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as f:
            for line in f:
                name, phone, email, address = line.strip().split(" | ")
                contacts.append({
                    "name": name,
                    "phone": phone,
                    "email": email,
                    "address": address
                })
    return contacts

# Save all contacts back to the file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        for contact in contacts:
            f.write(f"{contact['name']} | {contact['phone']} | {contact['email']} | {contact['address']}\n")

def display_contacts(contacts):
    if not contacts:
        slow_print("No contacts found.")
        return
    slow_print("Contact List:")
    for i, c in enumerate(contacts, 1):
        print(f"{i}. {c['name']} |  {c['phone']}")  

def display_full_contact(contact, index):
    print(f"{index}. {contact['name']} |  {contact['phone']} |  {contact['email']} |  {contact['address']}")

def add_contact(contacts):
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    address = input("Address: ")
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    save_contacts(contacts)
    slow_print(" Contact added successfully!")

def search_contact(contacts):
    query = input("Enter name or phone to search: ").lower()
    found = [c for c in contacts if query in c['name'].lower() or query in c['phone']]
    if found:
        slow_print("Search Results:")
        for i, c in enumerate(found, 1):
            display_full_contact(c, i)
    else:
        slow_print("No match found.")

def update_contact(contacts):
    query = input("Enter name or phone to update: ").lower()
    matched_indexes = [i for i, c in enumerate(contacts) if query in c['name'].lower() or query in c['phone']]

    if not matched_indexes:
        slow_print("No match found.")
        return

    slow_print("Matching Contacts:")
    for i, idx in enumerate(matched_indexes, 1):
        contact = contacts[idx]
        print(f"{i}. {contact['name']} |  {contact['phone']} |  {contact['email']} |  {contact['address']}")

    try:
        choice = int(input(" Enter serial_number of contact to update: "))
        if 1 <= choice <= len(matched_indexes):
            real_index = matched_indexes[choice - 1]
            contact = contacts[real_index]

            slow_print(" Leave blank to keep old value.")
            name = input(f"New name [{contact['name']}]: ") or contact['name']
            phone = input(f"New phone [{contact['phone']}]: ") or contact['phone']
            email = input(f"New email [{contact['email']}]: ") or contact['email']
            address = input(f"New address [{contact['address']}]: ") or contact['address']

            contacts[real_index] = {"name": name, "phone": phone, "email": email, "address": address}
            save_contacts(contacts)
            slow_print(" Contact updated successfully!")
        else:
            slow_print(" Invalid choice number.")
    except ValueError:
        slow_print(" Please enter a valid number.")

def delete_contact(contacts):
    display_contacts(contacts)
    try:
        index = int(input(" Enter contact serial_number to delete: ")) - 1
        if 0 <= index < len(contacts):
            confirm = input(f" Are you sure to delete {contacts[index]['name']}? (y/n): ").lower()
            if confirm == 'y':
                deleted = contacts.pop(index)
                save_contacts(contacts)
                slow_print(f" {deleted['name']} deleted.")
        else:
            slow_print(" Invalid number.")
    except ValueError:
        slow_print(" Please enter a valid number.")

def main():
    contacts = load_contacts()
    slow_print(" Welcome")

    while True:
        print("\n Menu:")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter choice (1–6): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            display_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            slow_print("ThankYou")
            break
        else:
            slow_print("Invalid choice. Try again.")

# Run 
main()
