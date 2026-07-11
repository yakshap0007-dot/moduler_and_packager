from datetime import datetime

class JournalManager:

    def __init__(self):
        self.file = "journal.txt"

    def add_entry(self):
        try:
            entry = input("\nEnter your journal entry:\n")
            f = open(self.file, "a")
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write("[" + time + "]\n")
            f.write(entry + "\n\n")
            f.close()
            print("\nEntry added successfully!")

        except PermissionError:
            print("Permission Denied!")

    def view_entries(self):
        try:
            f = open(self.file, "r")
            data = f.read()
            if data.strip() == "":
                print("\nNo journal entries found. Start by adding a new entry!")
            else:
                print("\nYour Journal Entries:")
                print("----------------------------------")
                print(data)
            f.close()

        except FileNotFoundError:
            print("\nError: The journal file does not exist. Please add a new entry first.")

    def search_entry(self):
        key = input("\nEnter a keyword or date to search: ")

        try:
            f = open(self.file, "r")
            data = f.read()
            f.close()

            if key.lower() in data.lower():

                print("\nMatching Entries:")
                print("----------------------------------")
                print(data)

            else:
                print("\nNo entries were found for the keyword:", key)

        except FileNotFoundError:
            print("\nError: The journal file does not exist. Please add a new entry first.")

    def delete_entries(self):
        answer = input("\nAre you sure you want to delete all entries? (yes/no): ")

        if answer.lower() == "yes":

            try:
                f = open(self.file, "w")
                f.close()

                print("\nAll journal entries have been deleted.")

            except FileNotFoundError:
                print("\nNo journal entries to delete.")

        else:
            print("\nDeletion Cancelled.")

obj = JournalManager()

while True:

    print("\nWelcome to Personal Journal Manager!")
    print("Please select an option:\n")

    print("1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")

    choice = input("\nUser Input: ")

    if choice == "1":
        obj.add_entry()

    elif choice == "2":
        obj.view_entries()

    elif choice == "3":
        obj.search_entry()

    elif choice == "4":
        obj.delete_entries()

    elif choice == "5":
        print("\nThank you for using Personal Journal Manager. Goodbye!")
        break

    else:
        print("\nInvalid option. Please select a valid option from the menu.")

