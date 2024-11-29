from contact_manager import ContactManager

def main_menu():
    manager = ContactManager()

    while True:
        print("--------------------------------------")
        print("-             Welcome!               -")
        print("--------------------------------------\n")
        print("\n")
        print("\n")
        print("\n--- Contact Book Management System ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Remove Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            manager.add_contact()
        elif choice == "2":
            manager.view_contacts()
        elif choice == "3":
            manager.search_contact()
        elif choice == "4":
            manager.remove_contact()
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()