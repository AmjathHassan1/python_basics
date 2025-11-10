import csv
import os
from datetime import datetime

class MenuPicker:
    def __init__(self):
        self.menu = {
            "1" : "view",
            "2" : "add",
            "3" : "delete",
            "4" : "update",
            "5" : "search",
            "6" : "top_students",
            "7" : "logout",
        }


    @staticmethod
    def show_menu():
        print("\nWelcome to Menu Picker")
        print("\nEnter 1 for View Students Record")
        print("Enter 2 for Add Student")
        print("Enter 3 for Update Student")
        print("Enter 4 for Delete Student")
        print("Enter 5 for Search Student")
        print("Enter 6 for Show Top Performing")
        print("Enter 7 for Log Out")

    def input_menu(self):
        try:
            menu = input("\nEnter Menu Picker: ")
            if menu not in list(self.menu.keys()):
                print("\nInvalid input. Please try again.")
                return False
            return menu
        except Exception as e:
            print("\nInvalid input. Please try again.")
            return False

class CrudStudent:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.fields = ['Name', 'Roll Number', 'Age', 'Department', 'Marks', 'Created On', 'Updated On']

        # Create file if not exists
        if not os.path.exists(self.csv_file):
            with open(self.csv_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(self.fields)

    def add_student(self):
        try:
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            dept = input("Enter Department: ")
            marks = input("Enter Marks: ")

            roll_number = 1
            # Logic to give Auto-generate student ID
            if os.path.getsize(self.csv_file) > 0:  # file not empty
                with open(self.csv_file, mode='r') as file:
                    reader = csv.DictReader(file)
                    roll_numbers = [int(row['Roll Number']) for row in reader if row['Roll Number'].isdigit()]
                    if roll_numbers:
                        roll_number = max(roll_numbers) + 1

            created_on = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            updated_on = created_on

            with open(self.csv_file, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([name, roll_number, age, dept, marks, created_on, updated_on])
            print(f"Student added successfully! (Assigned Roll No: {roll_number})\n")
            return True
        except Exception as e:
            print("\nInvalid input. Please try again.")
            return False

    def view_student(self):
        try:
            with open(self.csv_file, mode='r') as file:
                reader = csv.DictReader(file)
                print("\n--- Student Records ---")
                for row in reader:
                    print(f"Name: {row['Name']}, Roll No: {row['Roll Number']}, Age: {row['Age']}, "
                          f"Dept: {row['Department']}, Marks: {row['Marks']}, "
                          f"Created On: {row['Created On']}, Updated On: {row['Updated On']}")
                print("------------------------\n")
                return True
        except Exception as e:
            print("\nInvalid input. Please try again.")
            return False

    def update_student(self):
        try:
            roll_no = input("Enter Roll Number of the student to update: ")
            updated = False
            rows = []

            with open(self.csv_file, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['Roll Number'] == roll_no:
                        print("Enter new details (leave blank to keep current value):")
                        row['Name'] = input(f"Name ({row['Name']}): ") or row['Name']
                        row['Age'] = input(f"Age ({row['Age']}): ") or row['Age']
                        row['Department'] = input(f"Department ({row['Department']}): ") or row['Department']
                        row['Marks'] = input(f"Marks ({row['Marks']}): ") or row['Marks']
                        row['Updated On'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        updated = True
                    rows.append(row)

            if updated:
                with open(self.csv_file, mode='w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=self.fields)
                    writer.writeheader()
                    writer.writerows(rows)
                print("Student record updated!\n")
            else:
                print("Student not found.\n")
            return True
        except Exception as e:
            print("\nInvalid input. Please try again.")
            return False

    def delete_student(self):
        try:
            roll_no = input("Enter Roll Number of the student to delete: ")
            deleted = False
            rows = []

            with open(self.csv_file, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['Roll Number'] != roll_no:
                        rows.append(row)
                    else:
                        deleted = True

            if deleted:
                with open(self.csv_file, mode='w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=self.fields)
                    writer.writeheader()
                    writer.writerows(rows)
                print("Student deleted successfully!\n")
            else:
                print("Student not found.\n")
            return True
        except Exception as e:
            print("\nInvalid input. Please try again.")
            return False

    def search_student(self):
        try:
            keyword = input("Enter Name or Department to search: ").strip().lower()
            found = False

            with open(self.csv_file, mode='r') as file:
                reader = csv.DictReader(file)
                print("\n--- Search Results ---")
                for row in reader:
                    if (keyword in row['Name'].lower()) or (keyword in row['Department'].lower()):
                        print(f"Name: {row['Name']}, Roll No: {row['Roll Number']}, Age: {row['Age']}, "
                              f"Dept: {row['Department']}, Marks: {row['Marks']}")
                        found = True

            if not found:
                print("No students found matching the search.\n")
            print("------------------------\n")
            return True
        except Exception as e:
            print("\nInvalid input. Please try again.")
            return False

    def view_top_students(self):
        try:
            top_n = int(input("Enter how many top students to view: "))
            students = []

            with open(self.csv_file, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        marks = float(row['Marks'])
                        students.append(row)
                    except ValueError:
                        continue

            students.sort(key=lambda x: float(x['Marks']), reverse=True)

            print(f"\n--- Top {top_n} Students ---")
            for i, student in enumerate(students[:top_n], start=1):
                print(f"{i}. {student['Name']} ({student['Department']}) - Marks: {student['Marks']}")
            print("----------------------------\n")
            return True
        except Exception as e:
            print("\nInvalid input. Please try again.")
            return False