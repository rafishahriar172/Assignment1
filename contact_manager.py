import file_handler
from utils import validate_input

class ContactManager:
    def __init__(self):
        self.contacts = file_handler.load_contacts()

    def add_contact(self):
        print("\n--- Add Contact ---")
        name = validate_input("Enter Name: ", str)
        phone = validate_input("Enter Phone Number: ", int)
        email = input("Enter Email: ")
        address = input("Enter Address: ")

        if phone in [contact["Phone"] for contact in self.contacts]:
            print("Error: This phone number already exists!")
            return

        self.contacts.append({"Name": name, "Phone": phone, "Email": email, "Address": address})
        file_handler.save_contacts(self.contacts)
        print("Contact added successfully!")

    def view_contacts(self):
        print("\n--- All Contacts ---")
        if not self.contacts:
            print("No contacts available.")
            return

        for idx, contact in enumerate(self.contacts, start=1):
            print(f"{idx}. {contact['Name']} | {contact['Phone']} | {contact['Email']} | {contact['Address']}")

    def search_contact(self):
        print("\n--- Search Contact ---")
        search_term = input("Enter Name, Phone, Email, or Address to search: ").lower()
        results = [contact for contact in self.contacts if search_term in str(contact).lower()]

        if results:
            for idx, contact in enumerate(results, start=1):
                print(f"{idx}. {contact['Name']} | {contact['Phone']} | {contact['Email']} | {contact['Address']}")
        else:
            print("No matching contacts found.")

    def remove_contact(self):
        print("\n--- Remove Contact ---")
        self.view_contacts()
        try:
            idx = int(input("Enter the contact number to remove: ")) - 1
            if 0 <= idx < len(self.contacts):
                removed = self.contacts.pop(idx)
                file_handler.save_contacts(self.contacts)
                print(f"Removed contact: {removed['Name']}")
            else:
                print("Invalid contact number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
