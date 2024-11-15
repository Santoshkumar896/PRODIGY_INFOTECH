import json

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email
        }

    @staticmethod
    def from_dict(data):
        return Contact(data["name"], data["phone"], data["email"])


class ContactManager:
    def __init__(self, filename="contacts.json"):
        self.contacts = []
        self.filename = filename
        self.load_contacts()

    def add_contact(self):
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        email = input("Enter contact email address: ")
        contact = Contact(name, phone, email)
        self.contacts.append(contact)
        print("Contact added successfully.")
        self.save_contacts()

    def view_contacts(self):
        if not self.contacts:
            print("No contacts to display.")
            return
        print("\nContact List:")
        for idx, contact in enumerate(self.contacts, 1):
            print(f"{idx}. Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")
        print()

    def edit_contact(self):
        self.view_contacts()
        try:
            index = int(input("Enter the number of the contact to edit: ")) - 1
            if 0 <= index < len(self.contacts):
                contact = self.contacts[index]
                contact.name = input(f"Enter new name (current: {contact.name}): ") or contact.name
                contact.phone = input(f"Enter new phone (current: {contact.phone}): ") or contact.phone
                contact.email = input(f"Enter new email (current: {contact.email}): ") or contact.email
                print("Contact updated successfully.")
                self.save_contacts()
            else:
                print("Invalid contact number.")
        except ValueError:
            print("Please enter a valid number.")

    def delete_contact(self):
        self.view_contacts()
        try:
            index = int(input("Enter the number of the contact to delete: ")) - 1
            if 0 <= index < len(self.contacts):
                removed_contact = self.contacts.pop(index)
                print(f"Contact {removed_contact.name} deleted successfully.")
                self.save_contacts()
            else:
                print("Invalid contact number.")
        except ValueError:
            print("Please enter a valid number.")

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            json.dump([contact.to_dict() for contact in self.contacts], file)
        print("Contacts saved to file.")

    def load_contacts(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                self.contacts = [Contact.from_dict(item) for item in data]
            print("Contacts loaded from file.")
        except FileNotFoundError:
            print("No saved contacts found.")

    def main_menu(self):
        while True:
            print("\nContact Manager")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Edit Contact")
            print("4. Delete Contact")
            print("5. Exit")
            choice = input("Choose an option: ")
            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.view_contacts()
            elif choice == '3':
                self.edit_contact()
            elif choice == '4':
                self.delete_contact()
            elif choice == '5':
                print("Exiting Contact Manager. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

# Run the Contact Manager
contact_manager = ContactManager()
contact_manager.main_menu()
