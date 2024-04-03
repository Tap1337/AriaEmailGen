import random
import string
import os

class Loader:
    def update_progress(self, email, password):
        print(f"Generating {email} (Password: {password})")

def generate_credentials(num_credentials):
    credentials = []
    domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com"]
    for _ in range(num_credentials):
        username = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))
        domain = random.choice(domains)
        password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
        email = f"{username}@{domain}"
        credentials.append((email, password))
    return credentials

def save_to_file(credentials):
    with open("emails.txt", "w") as file:
        for email, password in credentials:
            file.write(f"Email: {email}, Password: {password}\n")

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
    print("Generating emails and passwords...")
    credentials = generate_credentials(num_credentials)
    save_to_file(credentials)
    loader = Loader()
    for email, password in credentials:
        loader.update_progress(email, password)
    print("Emails and passwords generated and saved to 'emails.txt'!")
    input("Press Enter to exit...")

if __name__ == "__main__":
    display_loader()
