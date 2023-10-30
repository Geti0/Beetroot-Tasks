# Task 1

# file = open('myfile.txt', mode='w')
# writing = file.write('Hello file world!')


# open_file = open('myfile.txt', mode='r')
# reading = open_file.read()
# print(reading)


# Task 2

import json

# Initialize the phonebook with data from a JSON file if it exists, or create an empty phonebook
def load_phonebook(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_phonebook(filename, phonebook):
    with open(filename, 'w') as file:
        json.dump(phonebook, file)

def add_entry(phonebook, entry):
    phonebook.append(entry)
    return "Entry added."

def search_by_field(phonebook, field, value):
    results = []
    for entry in phonebook:
        if entry[field].lower() == value.lower():
            results.append(entry)
    return results

def delete_entry(phonebook, phone):
    for entry in phonebook:
        if entry['telephone'] == phone:
            phonebook.remove(entry)
            return "Entry deleted."
    return "Entry not found."

def update_entry(phonebook, phone, new_entry):
    for entry in phonebook:
        if entry['telephone'] == phone:
            entry.update(new_entry)
            return "Entry updated."
    return "Entry not found."

def print_search_results(results):
    if results:
        print("Search Results:")
        for result in results:
            print(result)
    else:
        print("No matching records found.")

if __name__ == "__main__":
    phonebook_file = "phonebook.json"
    phonebook = load_phonebook(phonebook_file)

    while True:
        print("Phonebook Application")
        print("1. Add new entry")
        print("2. Search by first name")
        print("3. Search by last name")
        print("4. Search by full name")
        print("5. Search by telephone number")
        print("6. Search by city or state")
        print("7. Delete a record")
        print("8. Update a record")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            entry = {
                "first_name": input("First Name: "),
                "last_name": input("Last Name: "),
                "telephone": input("Telephone Number: "),
                "city": input("City: "),
                "state": input("State: ")
            }
            print(add_entry(phonebook, entry))

        elif choice == "2":
            first_name = input("Enter first name: ")
            results = search_by_field(phonebook, "first_name", first_name)
            print_search_results(results)

        elif choice == "3":
            last_name = input("Enter last name: ")
            results = search_by_field(phonebook, "last_name", last_name)
            print_search_results(results)

        elif choice == "4":
            full_name = input("Enter full name: ")
            results = []
            for entry in phonebook:
                if full_name.lower() in f"{entry['first_name']} {entry['last_name']}".lower():
                    results.append(entry)
            print_search_results(results)

        elif choice == "5":
            phone_number = input("Enter telephone number: ")
            results = search_by_field(phonebook, "telephone", phone_number)
            print_search_results(results)

        elif choice == "6":
            location = input("Enter city or state: ")
            results = search_by_field(phonebook, "city", location) + search_by_field(phonebook, "state", location)
            print_search_results(results)

        elif choice == "7":
            phone_number = input("Enter telephone number to delete: ")
            print(delete_entry(phonebook, phone_number))

        elif choice == "8":
            phone_number = input("Enter telephone number to update: ")
            entry = {
                "first_name": input("First Name: "),
                "last_name": input("Last Name: "),
                "telephone": input("Telephone Number: "),
                "city": input("City: "),
                "state": input("State: ")
            }
            print(update_entry(phonebook, phone_number, entry))

        elif choice == "9":
            save_phonebook(phonebook_file, phonebook)
            print("Phonebook saved. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
