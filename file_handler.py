import csv

FILE_NAME = "contacts.csv"

def load_contacts():
    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []

def save_contacts(contacts):
    with open(FILE_NAME, mode="w", newline="") as file:
        fieldnames = ["Name", "Phone", "Email", "Address"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contacts)
