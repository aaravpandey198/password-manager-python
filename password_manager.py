# ==============================
# PASSWORD MANAGER
# Version 1.1
# ==============================

# Display all saved passwords
def view():
    try:
        with open("sample_password.txt", "r") as f:
            print("\n" + "=" * 50)

            for line in f:
                data = line.rstrip()
                user, passwd = data.split("||")

                print(f"Account : {user}")
                print(f"Password: {passwd}")
                print("=" * 50)

    except FileNotFoundError:
        print("No passwords have been saved yet.")


# Add a new account and password
def add():
    acc = input("Enter account name: ").strip()
    passwd = input("Enter the password: ").strip()

    if not acc or not passwd:
        print("Account name and password cannot be empty.")
        return

    with open("sample_password.txt", "a") as f:
        f.write(f"{acc}||{passwd}\n")

    print("Password saved successfully!")


# ==============================
# MASTER PASSWORD AUTHENTICATION
# ==============================

try:
    with open("sample_master.txt", "r") as f:
        saved_password = f.read().strip()

except FileNotFoundError:
    print("Master password file not found.")
    exit()


master_password = input("Enter master password: ")

if master_password != saved_password:
    print("Wrong master password!")
    exit()

print("\nAccess Granted!")

# ==============================
# MAIN MENU
# ==============================

while True:

    print("\n========== PASSWORD MANAGER ==========")
    print("1. View Passwords (v)")
    print("2. Add Password (a)")
    print("3. Quit (q)")

    mode = input("\nEnter your choice: ").lower().strip()

    if mode == "q":
        print("Goodbye!")
        break

    elif mode == "a":
        add()

    elif mode == "v":
        view()

    else:
        print("Invalid option. Please try again.")