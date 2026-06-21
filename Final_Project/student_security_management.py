import re

FILE_NAME = "students.txt"


def load_students():
    students = []
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split("|")
                student = {
                    "id": parts[0],
                    "name": parts[1],
                    "branch": parts[2],
                    "email": parts[3],
                    "mfa_enabled": parts[4],
                    "password_length": parts[5],
                    "system_updated": parts[6],
                    "antivirus_installed": parts[7],
                    "security_score": parts[8],
                    "security_status": parts[9],
                }
                students.append(student)
    except FileNotFoundError:
        students = []
    return students


def save_students(students):
    with open(FILE_NAME, "w") as file:
        for s in students:
            line = "|".join([
                str(s["id"]),
                str(s["name"]),
                str(s["branch"]),
                str(s["email"]),
                str(s["mfa_enabled"]),
                str(s["password_length"]),
                str(s["system_updated"]),
                str(s["antivirus_installed"]),
                str(s["security_score"]),
                str(s["security_status"]),
            ])
            file.write(line + "\n")


def add_student(students):
    print("\n--- Add Student ---")
    student_id = input("Enter Student ID: ").strip()

    for s in students:
        if s["id"] == student_id:
            print(f"A student with ID {student_id} already exists.")
            return

    name = input("Enter Student Name: ").strip()
    branch = input("Enter Branch: ").strip()
    email = input("Enter Email Address: ").strip()

    if name == "" or branch == "" or email == "":
        print("Name, Branch and Email cannot be empty. Student not added.")
        return

    new_student = {
        "id": student_id,
        "name": name,
        "branch": branch,
        "email": email,
        "mfa_enabled": "None",
        "password_length": "None",
        "system_updated": "None",
        "antivirus_installed": "None",
        "security_score": "None",
        "security_status": "Not Assessed",
    }

    students.append(new_student)
    save_students(students)
    print(f"Student '{name}' (ID: {student_id}) added successfully.")


def view_students(students):
    print("\n--- All Students ---")
    if not students:
        print("No student records found.")
        return

    for s in students:
        print("--------------------------")
        print(f"ID: {s['id']}")
        print(f"Name: {s['name']}")
        print(f"Branch: {s['branch']}")
        print(f"Email: {s['email']}")
        print(f"Security Score: {s['security_score']}")
        print(f"Security Status: {s['security_status']}")

    print("--------------------------")
    print(f"Total Students: {len(students)}")


def search_student(students):
    print("\n--- Search Student ---")
    if not students:
        print("No student records found.")
        return

    print("1. Search by Name")
    print("2. Search by Student ID")
    option = input("Choose an option (1-2): ").strip()

    found = []

    if option == "1":
        name = input("Enter Name to search: ").strip().lower()
        found = [s for s in students if s["name"].lower() == name]
    elif option == "2":
        student_id = input("Enter Student ID to search: ").strip()
        found = [s for s in students if s["id"] == student_id]
    else:
        print("Invalid option.")
        return

    if not found:
        print("Record Not Found")
        return

    for s in found:
        print("--------------------------")
        print(f"ID: {s['id']}")
        print(f"Name: {s['name']}")
        print(f"Branch: {s['branch']}")
        print(f"Email: {s['email']}")
        print(f"Security Score: {s['security_score']}")
        print(f"Security Status: {s['security_status']}")
    print("--------------------------")


def delete_student(students):
    print("\n--- Delete Student ---")
    if not students:
        print("No student records found.")
        return

    student_id = input("Enter Student ID to delete: ").strip()

    for s in students:
        if s["id"] == student_id:
            confirm = input(f"Are you sure you want to delete {s['name']} (ID: {student_id})? (yes/no): ").strip().lower()
            if confirm == "yes":
                students.remove(s)
                save_students(students)
                print(f"Student ID {student_id} deleted successfully.")
            else:
                print("Deletion cancelled.")
            return

    print("Student ID not found.")


def calculate_security_score(mfa_enabled, password_length, system_updated, antivirus_installed):
    score = 0

    if mfa_enabled == "yes":
        score += 25

    if password_length >= 12:
        score += 25
    elif password_length >= 8:
        score += 15
    else:
        score += 5

    if system_updated == "yes":
        score += 25

    if antivirus_installed == "yes":
        score += 25

    return score


def get_security_status(score):
    if score >= 90:
        return "Excellent"
    elif score >= 70:
        return "Good"
    elif score >= 50:
        return "Moderate"
    else:
        return "Poor"


def security_assessment(students):
    print("\n--- Security Assessment ---")
    if not students:
        print("No student records found.")
        return

    student_id = input("Enter Student ID to assess: ").strip()
    target = None
    for s in students:
        if s["id"] == student_id:
            target = s
            break

    if target is None:
        print("Student ID not found.")
        return

    mfa_input = input("Is MFA Enabled? (yes/no): ").strip().lower()

    while True:
        try:
            password_length = int(input("Password Length: ").strip())
            break
        except ValueError:
            print("Please enter a valid number.")

    updated_input = input("System Updated? (yes/no): ").strip().lower()
    antivirus_input = input("Antivirus Installed? (yes/no): ").strip().lower()

    score = calculate_security_score(mfa_input, password_length, updated_input, antivirus_input)
    status = get_security_status(score)

    target["mfa_enabled"] = mfa_input
    target["password_length"] = password_length
    target["system_updated"] = updated_input
    target["antivirus_installed"] = antivirus_input
    target["security_score"] = score
    target["security_status"] = status

    save_students(students)

    print(f"\nSecurity Score: {score}/100")
    print(f"Status: {status}")


def generate_report(students):
    print("\n--- Security Report ---")
    if not students:
        print("No student records found.")
        return

    total_students = len(students)
    assessed = [s for s in students if s["security_score"] != "None"]

    print(f"Total Students: {total_students}")
    print("\nSecurity Scores:")
    for s in students:
        print(f"{s['name']} (ID: {s['id']}): {s['security_score']}")

    if assessed:
        total_score = sum(int(s["security_score"]) for s in assessed)
        average_score = total_score / len(assessed)
        print(f"\nAverage Security Score: {average_score:.2f}")
    else:
        print("\nAverage Security Score: No students assessed yet.")

    poor_students = [s for s in assessed if s["security_status"] == "Poor"]
    print("\nStudents with Poor Security Ratings:")
    if poor_students:
        for s in poor_students:
            print(f"{s['name']} (ID: {s['id']}) - Score: {s['security_score']}")
    else:
        print("None")


def password_strength_checker():
    print("\n--- Password Strength Checker ---")
    password = input("Enter a password to check: ")

    length_ok = len(password) >= 8
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    score = sum([length_ok, has_upper, has_lower, has_digit, has_special])

    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    print(f"Password Strength: {strength}")


def username_generator():
    print("\n--- Username Generator ---")
    name = input("Enter your full name: ").strip()
    birth_year = input("Enter your birth year (e.g. 2003): ").strip()

    first_name = name.split(" ")[0].lower() if name else "user"
    username = f"{first_name}{birth_year}"

    print(f"Generated Username: {username}")


def login_validation():
    print("\n--- Login Validation ---")
    stored_username = "admin"
    stored_password = "Admin@123"

    username = input("Enter Username: ").strip()
    password = input("Enter Password: ").strip()

    if username == stored_username and password == stored_password:
        print("Login Successful")
    else:
        print("Login Failed: Invalid Username or Password")


def main():
    students = load_students()

    while True:
        print("\n==========================")
        print(" Student Security Manager")
        print("==========================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Security Assessment")
        print("6. Generate Report")
        print("7. Password Strength Checker")
        print("8. Username Generator")
        print("9. Login Validation")
        print("10. Exit")

        choice = input("Enter your choice (1-10): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            security_assessment(students)
        elif choice == "6":
            generate_report(students)
        elif choice == "7":
            password_strength_checker()
        elif choice == "8":
            username_generator()
        elif choice == "9":
            login_validation()
        elif choice == "10":
            print("Exiting Student Security Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 10.")


if __name__ == "__main__":
    main()