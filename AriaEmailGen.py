import random
import string
import os

class Loader:
    def update_progress(self, email):
        print(f"Generating {email}")

def generate_credentials(num_credentials):
    credentials = []
    domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com"]
    for i in range(1, num_credentials + 1):
        random_char = random.choice(string.ascii_letters + string.digits)
        domain = random.choice(domains)
        email = f"example{i}{random_char}@{domain}"
        credentials.append(email)
    return credentials

def save_to_file(credentials):
    with open("emails.txt", "w") as file:
        for email in credentials:
            file.write(f"Email: {email}\n")

def display_loader():
    print('''
                                                  
 _____     _     _____           _ _ _____         
|  _  |___|_|___|   __|_____ ___|_| |   __|___ ___ 
|     |  _| | .'|   __|     | .'| | |  |  | -_|   |
|__|__|_| |_|__,|_____|_|_|_|__,|_|_|_____|___|_|_|
          
     github.com/Tap1337 | discord.gg/ariacc
                                                  
    ''')
    num_credentials = int(input("Enter the number of credentials to generate: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    print('''
                                                  
 _____     _     _____           _ _ _____         
|  _  |___|_|___|   __|_____ ___|_| |   __|___ ___ 
|     |  _| | .'|   __|     | .'| | |  |  | -_|   |
|__|__|_| |_|__,|_____|_|_|_|__,|_|_|_____|___|_|_|
          
     github.com/Tap1337 | discord.gg/ariacc
                                                  
    ''')
    print("Generating emails...")
    credentials = generate_credentials(num_credentials)
    save_to_file(credentials)
    loader = Loader()
    for email in credentials:
        loader.update_progress(email)
    print("Emails generated and saved to 'emails.txt'!")
    input("Press Enter to exit...")

if __name__ == "__main__":
    display_loader()
