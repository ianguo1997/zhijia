import sys
import re
import ast  # 导入 ast 模块来解析存储的列表
import re
import ast


class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def verify_credentials(self):
        # Check email format
        email_regex = re.compile(r"[a-zA-Z]+(?:\.[a-zA-Z]+)?@university\.com")
        if not email_regex.match(self.email):
            print("The format of Email Address is WRONG")
            return False

        try:
            with open("students.data", "r") as file:
                content = file.read()
                students_list = ast.literal_eval(content)  # 将字符串解析为列表

                for student_data in students_list:
                    email, password, *others = student_data
                    if self.email == email:
                        if self.password == password:
                            print("Credentials verified!")
                            return True
                        else:
                            print("The entered Password is INCORRECT")
                            return False

                print(
                    "The entered Email Address does NOT EXIST, Please register first!"
                )
                return False

        except FileNotFoundError:
            print("No students data found.")
            return False
        except (
            SyntaxError
        ) as e:  # 如果文件内容不是有效的 Python 结构，ast.literal_eval 会抛出 SyntaxError
            print(f"Error parsing the data file: {e}")
            return False

    def login(self):
        if self.verify_credentials():
            print("Login successful!")
            return True
        else:
            print("Login failed!")


class Student(User):
    def __init__(self, email, password):
        super().__init__(email, password)
        self.name = ""
        self.student_id = ""
        self.enrollment_list = []

    def view_subjects(self):
        # Logic to view subjects
        pass

    def change_password(self):
        self.new_password = input("Enter your new password: ")
        self.check_password = input("Repeat your new password: ")

        if self.check_password == self.new_password:
            try:
                # 读取文件内容
                with open("students.data", "r") as file:
                    students_list = ast.literal_eval(file.read())

                # 查找并更新密码
                for student_data in students_list:
                    email, password, *others = student_data
                    if email == self.email:
                        student_data[1] = self.new_password  # 更新密码
                        print("Password changed successfully!")

                # 将更新后的列表写回文件
                with open("students.data", "w") as file:
                    file.write(str(students_list))

            except FileNotFoundError:
                print("Students data file not found.")
            except SyntaxError:
                print("Error parsing the data file.")
            # 应该添加更多的异常处理来处理可能的错误
        else:
            print("Inconsistent new password!")

    def register(self):
        # 获取学生信息
        self.name = input("Enter your name: ")
        # self.student_id = input("Enter your student ID: ")

        set_email = input("please set your email: ")
        set_password = input("please set your password: ")
        self.email = set_email
        self.password = set_password
        # 验证邮箱和密码是否已经设置
        if not self.email or not self.password:
            print("Error: Email or password is not set.")
            return False

        new_student_data = [self.email, self.password, self.name]

        try:
            # 读取现有的数据文件
            with open("students.data", "r") as file:
                content = file.read()
                if content:
                    students_list = ast.literal_eval(content)
                    # 检查学生是否已经注册
                    for student in students_list:
                        if student[0] == self.email:
                            print("A user with this email already exists.")
                            return False
                else:
                    students_list = []

            # 添加新学生到列表
            students_list.append(new_student_data)

            # 写回到文件
            with open("students.data", "w") as file:
                file.write(str(students_list))

            print(f"Student {self.name} registered successfully.")
            return True

        except FileNotFoundError:
            print("Students data file not found.")
            return False
        except SyntaxError:
            print("Error parsing the data file.")
            return False
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return False

    def view_enrollment(self):
        # Logic to view enrollment
        pass

    def view_enrollment_list(self):
        # Logic to view enrollment list
        pass

    def verify_amount_enrollment(self):
        # Logic to verify amount enrollment
        pass


class Admin(User):
    def __init__(self, email, password, name, user_id):
        super().__init__(email, password)
        self.name = name
        self.user_id = user_id

    def view_all_students(self):
        # Logic to view all students
        pass

    def clear_student_data(self, student_id):
        # Logic to clear student data
        pass

    def organize_by_grade(self, mark):
        # Logic to organize students by grade
        if mark >= 85:
            grade = "HD"
        elif mark >= 75:
            grade = "D"
        elif mark >= 65:
            grade = "C"
        elif mark >= 50:
            grade = "P"
        else:
            grade = "Z"
        return grade


if __name__ == "__main__":
    main_menu()
