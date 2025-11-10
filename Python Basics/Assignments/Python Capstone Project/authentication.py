import csv

class Authentication:
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def authenticate(self, username, password):
        with open(self.csv_file, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['email'] == username and row['password'] == password:
                    print(f"\nLogin successful! Welcome, {row['first_name']} {row['last_name']}.\n  ")
                    return {
                        "first_name": row['first_name'],
                        "last_name": row['last_name'],
                        "role": row['role'],
                        "email": row['email'],
                        "subject": row['subject'],
                    }

        print("Invalid username or password.")
        return False