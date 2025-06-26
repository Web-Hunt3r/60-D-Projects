import sys
import time
import random
from datetime import datetime, timedelta

print("     --------Welcome to PassKey by WebH--------")
print("            | Your Passwords. My Duty |        ")


generated_passkey=[]
def passkey(pw_length):
    keys = 'qwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()_+-=[];:,.<>/?`'
    pwd = ''
    for _ in range(pw_length):
        pwd += random.choice(keys)
    return pwd

print("\n 0. View Saved Passwords"
      "\n 1. Add a New Password"
      "\n 2. Remove a Password"
      "\n 3. Mark Expired Passwords (30+ days)"
      "\n 4. Exit\n")


while True:
    choice = input("Your Choice = ")

    if choice == "0":
        print("\n --- Your Stored Passwords ---\n")
        if not generated_passkey:
            print("No passwords saved yet!\n")
        else:
            for index, saved in enumerate(generated_passkey, start=1):
                app = saved['site']
                pwd = saved['password']
                date = saved['created']
                expired = saved['expired']
                status = "❌ Expired" if expired else "✅ Active"
                print(f"{index}. [{status}] {app}")
                print(f"    ↪ {pwd} (Added on {date.strftime('%Y-%m-%d')})")
            print()

    elif choice == "1":
        pwd_name = input("Enter the name of the site: ")
        try:
            pw_length = int(input("Enter password length: "))
        except ValueError:
            print("Invalid number, Generating 12 characters password instead...")
            pw_length = 12

        pwd = passkey(pw_length)
        generated_passkey.append({
            'site': pwd_name,
            'password': pwd,
            'created': datetime.now(),
            'expired': False })
        print(f"Password for '{pwd_name}' added: {pwd}\n")

    elif choice == "2":
        if not generated_passkey:
            print("No passwords found for removal!\n")
        else:
            for index, saved in enumerate(generated_passkey, start=1):
                print(f"{index}. {saved['site']}")
            try:
                idx = int(input("Enter the number of the password to remove: ")) - 1
                if 0 <= idx < len(generated_passkey):
                    removed = generated_passkey.pop(idx)
                    print(f"Removed password for: {removed['site']}\n")
                else:
                    print("Invalid number!\n")
            except ValueError:
                print("TInvalid Input! \n")

    elif choice == "3":
        today = datetime.now()
        expired_count = 0
        for saved in generated_passkey:
            if not saved['expired']:
                age = today - saved['created']
                if age.days >= 30:
                    saved['expired'] = True
                    expired_count += 1
        print(f"Marked {expired_count} password(s) as expired.\n")

    elif choice == "4":
        print("Exiting ./WebH_PassKeys  \n ")
        sys.exit(0)

    else:
        print("[MENU] 0-4 onlyyy, oakyyyyy🙂 okayyyy??🤨\n")
