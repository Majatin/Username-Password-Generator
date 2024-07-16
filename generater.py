import json
import datetime
import random
import string

def generate_username(first_name, last_name, birthday):
     # Combine first name, last name, and birthday
     username = f"{first_name[0].lower()}{last_name[:4].lower()}{birthday.strftime('%m%d')}"
     return username

def is_username_unique(username, existing_usernames):
     return username not in existing_usernames

def generate_password():
    # Create a list of characters to choose from.
    characters = string.ascii_letters + string.digits + string.punctuation
    passwords = []
    for i in range(15):
        password = ''.join(random.choice(characters) for i in range(15))
        passwords.append(password)
    # Return a random password from the list.
    return random.choice(passwords)

def main():
     # Load existing usernames from JSON file (if available)
     try:
         with open("usernames.json", "r") as json_file:
             existing_data = json.load(json_file)
             # Get usernames from the loaded data
             existing_usernames = list(existing_data.keys())  # Extract usernames as a list
     except FileNotFoundError:
         existing_data = {}
         existing_usernames = []

     while True:
         # Input user details
         first_name = input("Enter your first name: ")
         last_name = input("Enter your last name: ")
         birthday_str = input("Enter your birthday (in MM/DD/YY format): ")
         birthday = datetime.datetime.strptime(birthday_str, "%m/%d/%Y")

         # Generate unique username
         unique_username = generate_username(first_name, last_name, birthday)

         if is_username_unique(unique_username, existing_usernames):
             print(f"Unique username: {unique_username}")

             # Create a dictionary to store usernames
             usernames_dict = {
                 "first_name": first_name,
                 "last_name": last_name,
                 "birthday": birthday_str,
                 "username": unique_username,
                 "password": generate_password(),
             }

             # Confirmation step
             print("\nPlease confirm your information:")
             print(f"  First Name: {usernames_dict['first_name']}")
             print(f"  Last Name: {usernames_dict['last_name']}")
             print(f"  Birthday: {usernames_dict['birthday']}")
             print(f"  Username: {usernames_dict['username']}")
             print(f". Password: {usernames_dict['password']}")

             confirmation = input("Is this information correct? (yes/no): ").lower().strip()
             if confirmation == 'yes':
                 # Append to existing data (now a dictionary)
                 existing_data[unique_username] = usernames_dict  # Use unique username as key

                 # Serialize the updated data to a JSON file
                 with open("usernames.json", "w") as json_file:
                     json.dump(existing_data, json_file, indent=4)

                 print("Usernames saved to usernames.json")
                 break
             else:
                 print("Please try again.")
         else:
             print("Error: Username already exists. Please try again.")

if __name__ == "__main__":
     main()

# Finally, a function to give us the ability to add another name, or close the program.

def add_another_name():
    while True:
        add_another = input("Do you want to add another name? (yes/no):").lower().strip()
        if add_another == 'yes':
            main()
        elif add_another == 'no':
            print("Thank you for using the Username/Password Generator. Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

# Call the function to add another name or close the program.

add_another_name()