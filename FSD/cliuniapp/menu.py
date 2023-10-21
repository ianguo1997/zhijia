import sys
from cliuniapp.user import User, Student


def main_menu():
    while True:
        print("(A) Admin\n(S) Student\n(X) exit")
        choice = input("Choose an option: ")
        if choice.upper() == "A":
            admin_session()
        elif choice.upper() == "S":
            student_session()
        elif choice.upper() == "X":
            sys.exit()
        else:
            print("Invalid choice")


def student_session():
    while True:
        input_email = str(input("Input Email: "))
        input_password = str(input("Input Password: "))
        user = User(input_email, input_password)
        student = Student(input_email, input_password)
        # Attempt to login
        if user.login():
            break
        else:
            print("Do you want to try again?")
            quit_login = input("(Yes/No): ")
            if quit_login.lower() == "yes":
                True
            else:
                break

    while True:
        print(
            "(e) enroll subjects\n(c) cancel subjects\n(s) show enrollment subjects\n(p) change password\n(r) register\n(x) exit"
        )
        choice = input("Choose an option: ")
        if choice == "e":
            # Implement clear data functionality
            pass
        elif choice == "c":
            # Implement group students functionality
            pass
        elif choice == "s":
            # Implement partition students functionality
            pass
        elif choice == "p":
            student.change_password()
        elif choice == "r":
            student.register()
        elif choice == "x":
            break
        else:
            print("Invalid choice")


def admin_session():
    while True:
        print(
            "(c) clear data\n(g) group students\n(p) partition students\n(r) remove student\n(s) show students\n(x) exit"
        )
        choice = input("Choose an option: ")
        if choice == "c":
            # Implement clear data functionality
            pass
        elif choice == "g":
            # Implement group students functionality
            pass
        elif choice == "p":
            # Implement partition students functionality
            pass
        elif choice == "r":
            # Implement remove student functionality
            pass
        elif choice == "s":
            # Implement show students functionality
            pass
        elif choice == "x":
            break
        else:
            print("Invalid choice")
