# ================================
# 📋 Contact Book - by Solomon
# ================================
import json
import os

FILENAME = "contacts.json"

# Load contacts from file when program starts
def load_contacts():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return {}

# Save contacts to file after every change
def save_contacts():
    with open(FILENAME, "w") as f:
        json.dump(contacts, f)

contacts = load_contacts()


contacts = {}

def add_contact():
    name = input("Enter name: ").capitalize()
    if name in contacts:
        print(f"⚠️  {name} already exists!")
        return
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    contacts[name] = {"phone": phone, "email": email}
    save_contacts()
    print(f"✅ {name} saved successfully!")

def view_contacts():
    if len(contacts) == 0:
        print("📭 No contacts yet!")
        input("\nPress Enter to continue...")   
        return
    print("\n📋 All Contacts:")
    print("-" * 30)
    for name, info in contacts.items():
        print(f"👤 {name}")
        print(f"   📞 {info['phone']}")
        print(f"   📧 {info['email']}")
        print("-" * 30)
    input("\nPress Enter to continue...")      
def search_contact():
    name = input("Enter name to search: ").capitalize()
    if name in contacts:
        print(f"\n👤 {name}")
        print(f"   📞 {contacts[name]['phone']}")
        print(f"   📧 {contacts[name]['email']}")
    else:
        print(f"❌ {name} not found!")

def delete_contact():
    name = input("Enter name to delete: ").capitalize()
    if name in contacts:
        contacts.pop(name)
        save_contacts()
        print(f"🗑️  {name} deleted!")
    else:
        print(f"❌ {name} not found!")

def main_menu():
    while True:
        print("\n=== 📋 Contact Book ===")
        print("1. Add contact")
        print("2. View all contacts")
        print("3. Search contact")
        print("4. Delete contact")
        print("5. Quit")

        choice = input("Choose (1-5): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("👋 Goodbye Solomon!")
            break
        else:
            print("⚠️  Please choose 1 to 5")

# Start the program
main_menu()