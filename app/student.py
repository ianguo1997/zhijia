import re
import ast  # 导入 ast 模块来解析存储的列表
from app import STUDENT_DB,SUBJECT_LIST,GRADE
import random

# stephen@university.com
class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login(self):
        while True:
            if self.verify_credentials():
                return True
            else:
                print("Login failed!")
                print("Do you want to try again?")
                quit_login = input("(Yes/No): ")
                if quit_login.lower() == "yes":
                    True
                else:
                    break
                    return False

    def verify_credentials(self):
        # Check email format
        email_regex = re.compile(r"[a-zA-Z]+(?:\.[a-zA-Z]+)?@university\.com")
        if not email_regex.match(self.email):
            print("\033[91m{}\033[0m".format(
                f'{"":8}Incorrect email or password format'))
            return False
        else:
            print("\033[93m{}\033[0m".format(
                f'{"":8}email and password formats acceptable'))

        try:
            with open(STUDENT_DB, 'r') as file:
                content = file.read()
                students_list = ast.literal_eval(content)  # 将字符串解析为列表
                for student_data in students_list:
                    email, password, *others = student_data
                    if self.email == email:
                        if self.password == password:
                            return True
                        else:
                            print("The entered Password is INCORRECT")
                            return False

                print("\033[91m{}\033[0m".format(
                    f'{"":8}Student does not exist'))
                return False

        except FileNotFoundError:
            print("No students data found.")
            return False
        except SyntaxError as e:  # 如果文件内容不是有效的 Python 结构，ast.literal_eval 会抛出 SyntaxError
            print(f"Error parsing the data file: {e}")
            return False

    def register(self):
        email_regex = re.compile(r"[a-zA-Z]+(?:\.[a-zA-Z]+)?@university\.com")
        password_regex = re.compile(r"^[A-Z][a-zA-Z]{5,}[0-9]{3,}")    
        if not email_regex.match(self.email):
            if not password_regex.match(self.password):
                print("\033[91m{}\033[0m".format(
                    f'{"":8}Incorrect email or password format'))
                return False
        else:
            self.name = str(input(f'{"":8}Name: '))
            new_student_data = [self.email, self.password, self.name, random.randint(700000,799999)]

        try:
            # 读取现有的数据文件
            with open(STUDENT_DB, "r") as file:
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
            with open(STUDENT_DB, "w") as file:
                file.write(str(students_list))

            print("\033[91m{}\033[0m".format(
                f'{"":8}Enrolling Student {self.name}'))
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


class Student(User):
    def __init__(self, email, password):
        super().__init__(email, password)
        self.name = ''
        self.student_id = ''
        self.enrollment_list = []

    def student_course_menu(self):
        while True:
            choice = input(
                f'{"":16}\033[96mStudent Course Menu (c/e/r/s/x): \033[0m')
            if choice == "c":
                self.change_password()
            elif choice == "e":
                # Implement group students functionality
                self.enroll_subject()
                pass
            elif choice == "r":
                # Implement partition students functionality
                pass
            elif choice == "s":
                 self.view_subjects()
    
            elif choice == "x":
                break
            else:
                print("Invalid choice")

    def enroll_subject(self):
        try:
            # 读取现有的数据文件
            with open(STUDENT_DB, "r") as file:
                content = file.read()
                if content:
                    students_list = ast.literal_eval(content)
                    # 检查学生是否已经注册
                    for student in students_list:
                        if student[0] == self.email:
                            picked_class = random.choice(SUBJECT_LIST)
                            grade = random.choice(list(GRADE.keys()))
                            mark = random.randint(GRADE[grade][0], GRADE[grade][1])
                            if len(student)>4:
                                if len(student[4])>=4:
                                    print("\033[91m{}\033[0m".format(f'{"":16}Already registered 4 subjects. Maximum 4 subjects can be registered.'))
                                    print("")
                                    return False
                                if picked_class in student[4]:
                                    print("\033[91m{}\033[0m".format(f'{"":16}Subject-{picked_class} has already been enrolled'))
                                    return False
                                student[4].append({'SUBJECT':picked_class,'GRADE':grade,'MARK':mark})
                                print("\033[93m{}\033[0m".format(f'{"":16}Enrolling in Subject-{picked_class}'))
                                print("\033[93m{}\033[0m".format(f'{"":16}You have now enrolled in {len(student[4])} out of 4 subjects'))
                            elif len(student)<=4:
                                student.append([{'SUBJECT':picked_class,'GRADE':grade,'MARK':mark}])
                                print("\033[93m{}\033[0m".format(f'{"":16}Enrolling in Subject-{picked_class}'))
                                print("\033[93m{}\033[0m".format(f'{"":16}You have now enrolled in 1 out of 4 subjects'))
                else:
                    students_list = []

            # 写回到文件
            with open(STUDENT_DB, "w") as file:
                file.write(str(students_list))

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

    def view_subjects(self):
        try:
            # 读取现有的数据文件
            with open(STUDENT_DB, "r") as file:
                content = file.read()
                if content:
                    students_list = ast.literal_eval(content)
                    # 检查学生是否已经注册
                    for student in students_list:
                        if student[0] == self.email:
                            if len(student)>4:
                                print("\033[93m{}\033[0m".format(f'{"":16}Showing {len(student[4])} subjects'))
                                for sj in student[4]:
                                    sj_val = sj['SUBJECT']
                                    sj_gd = sj['GRADE']
                                    sj_mk = sj["MARK"]
                                    print(f'{"":16}[ Subject::{sj_val} -- mark = {sj_mk} -- grade = {sj_gd} ]')
                            elif len(student)<=4:
                                print("\033[93m{}\033[0m".format(f'{"":16}Showing 0 subjects'))

                else:
                    students_list = []

        except FileNotFoundError:
            print("Students data file not found.")
        except SyntaxError:
            print("Error parsing the data file.")
            return False
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return False

    def change_password(self):
        self.new_password = input("Enter your new password: ")
        self.check_password = input("Repeat your new password: ")

        if self.check_password == self.new_password:
            try:
                # 读取文件内容
                with open(STUDENT_DB, "r") as file:
                    students_list = ast.literal_eval(file.read())

                # 查找并更新密码
                for student_data in students_list:
                    email, password, *others = student_data
                    if email == self.email:
                        student_data[1] = self.new_password  # 更新密码
                        print("Password changed successfully!")

                # 将更新后的列表写回文件
                with open(STUDENT_DB, "w") as file:
                    file.write(str(students_list))

            except FileNotFoundError:
                print("Students data file not found.")
            except SyntaxError:
                print("Error parsing the data file.")
            # 应该添加更多的异常处理来处理可能的错误
        else:
            print("Inconsistent new password!")

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
    def __init__(self):
        pass
        
    def admin_menu(self):
        while True:
            choice = input(
                f'{"":8}\033[96mAdmin System (c/g/p/r/s/x): \033[0m')
            if choice == "c":
                self.clear_student_data()
            elif choice == "g":
                self.grade_grouping()
            elif choice == "p":
                self.pass_or_fail()
            elif choice == "r":
                self.remove_student_id()
            elif choice == "s":
                self.student_list()
            elif choice == "x":
                break
            else:
                print("Invalid choice")

    def clear_student_data(self):
        try:
            print("\033[93m{}\033[0m".format(f'{"":8}Clearing students database'))
            quit_login = input("\033[91m{}\033[0m".format(f'{"":8}Are you sure you want to clear the database (Y)ES/ (N)O:'))
            if quit_login.lower() == "y":
            # 写回到文件
                with open(STUDENT_DB, "w") as file:
                    file.write(str([]))
                print("\033[93m{}\033[0m".format(f'{"":8}Student data cleared'))
                return True
            else:
                return False

        except FileNotFoundError:
            print("Students data file not found.")
            return False
        except SyntaxError:
            print("Error parsing the data file.")
            return False
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return False

   
    def grade_grouping(self):
        try:
            # 读取现有的数据文件
            with open(STUDENT_DB, "r") as file:
                content = file.read()
                if content:
                    students_list = ast.literal_eval(content)
                    # 检查学生是否已经注册
                    print("\033[93m{}\033[0m".format(f'{"":8}Grade Grouping'))
                    length_list = [len(student) for student in students_list]
                    if max(length_list)<=4:
                        print(f'{"":16}< Nothing to Display >')
                        return False
                    for student in students_list:
                        if len(student)>4:
                            st_name = student[2]
                            st_id = student[3]
                            st_mk = []
                            for sj in student[4]:
                                st_mk.append(sj["MARK"])
                            st_mk = sum(st_mk) / len(st_mk)
                            for gd in GRADE:
                                if st_mk>=GRADE[gd][0] and st_mk<GRADE[gd][1]+1:
                                    st_gd = gd
                            print(f'{"":8}{st_gd} --> [{st_name} :: {st_id} --> GRADE: {st_gd} - MARK: {st_mk}]')

                else:
                    students_list = []

        except FileNotFoundError:
            print("Students data file not found.")
        except SyntaxError:
            print("Error parsing the data file.")
            return False
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return False

    def pass_or_fail(self):
        try:
            # 读取现有的数据文件
            with open(STUDENT_DB, "r") as file:
                content = file.read()
                if content:
                    students_list = ast.literal_eval(content)
                    # 检查学生是否已经注册
                    print("\033[93m{}\033[0m".format(f'{"":8}PASS/FILE Partition'))
                    length_list = [len(student) for student in students_list]
                    if max(length_list)<=4:
                        print(f'{"":16}< Nothing to Display >')
                        return False
                    pass_list,fail_list = [],[]
                    pass_result=''
                    fail_result=''
                    for student in students_list:
                        if len(student)>4:
                            st_name = student[2]
                            st_id = student[3]
                            st_mk = []
                            
                            for sj in student[4]:
                                st_mk.append(sj["MARK"])
                            st_mk = sum(st_mk) / len(st_mk)
                            for gd in GRADE:
                                if st_mk>=GRADE[gd][0] and st_mk<GRADE[gd][1]+1:
                                    st_gd = gd
                            if st_gd == 'F':
                                fail_list.append(f'{st_name} :: {st_id} --> GRADE: {st_gd} - MARK: {st_mk}')              
                            else:
                                pass_list.append(f'{st_name} :: {st_id} --> GRADE: {st_gd} - MARK: {st_mk}')
                    pass_result =  ','.join(pass_list) if pass_list!=[] else ''
                    fail_result =  ','.join(fail_result) if fail_result!=[] else ''
                    print(f'{"":8}FAIL --> [{fail_result}]')
                    print(f'{"":8}PASS --> [{pass_result}]')

                else:
                    students_list = []

        except FileNotFoundError:
            print("Students data file not found.")
        except SyntaxError:
            print("Error parsing the data file.")
            return False
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return False

    def remove_student_id(self):
        try:
            student_id_to_be_removed = input(f'{"":8}Remove by ID:')
            # 读取现有的数据文件
            with open(STUDENT_DB, "r") as file:
                content = file.read()
                if content:
                    students_list = ast.literal_eval(content)
                    student_id_list= [student[3] for student in students_list] 

                    if int(student_id_to_be_removed) not in student_id_list:
                        print("\033[91m{}\033[0m".format(f'{"":8}Student {student_id_to_be_removed} does not exist'))
                        return False
                    # 检查学生是否已经注册
                    for student in students_list:
                        if student[3] == int(student_id_to_be_removed):
                            students_list.remove(student)
                            print("\033[93m{}\033[0m".format(f'{"":8}Removing Student {student_id_to_be_removed} Account')) 
                else:
                    students_list = []

            # 写回到文件
            with open(STUDENT_DB, "w") as file:
                file.write(str(students_list))
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
    
    def student_list(self):
        try:
            # 读取现有的数据文件
            with open(STUDENT_DB, "r") as file:
                content = file.read()
                if content:
                    students_list = ast.literal_eval(content)
                    # 检查学生是否已经注册
                    print("\033[93m{}\033[0m".format(f'{"":8}Student List'))
                    if students_list==[]:
                        print(f'{"":16}< Nothing to Display >')
                    else:
                        for student in students_list:
                            print(f'{"":8}{student[2]} :: {student[3]} --> Email: {student[0]}')
                else:
                    students_list = []

        except FileNotFoundError:
            print("Students data file not found.")
        except SyntaxError:
            print("Error parsing the data file.")
            return False
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return False