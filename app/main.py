from .student import Student,User,Admin
import sys

def main_menu():
    while True:
        choice = input(
            "\033[96mUniversity System: (A)dmin,  (S)tudent,  or X : \033[0m")
        if choice.upper() == "A":
            user = Admin()
            user.admin_menu()
        elif choice.upper() == "S":
            student_session()
        elif choice.upper() == "X":
            print("\033[93m{}\033[0m".format("Thank You"))
            sys.exit()
        else:
            print("Invalid choice")

def student_session():

    while True:
        choice = input(f'{"":8}\033[96mStudent System (l/r/x): \033[0m')
        if choice.lower() == "l":
            print("\033[92m{}\033[0m".format(f'{"":8}Student Sign In'))
            email = str(input(f'{"":8}Email: '))
            password = str(input(f'{"":8}Input Password: '))
            user = User(email, password)
            if user.login():
                user = Student(email, password)
                user.student_course_menu()
        elif choice.lower() == "r":
            print("\033[92m{}\033[0m".format(f'{"":8}Student Sign Up'))
            email = str(input(f'{"":8}Email: '))
            password = str(input(f'{"":8}Input Password: '))
            user = User(email, password)
            user.register()
        elif choice.lower() == "x":
            break
        else:
            print("Invalid choice")

