"""read and write data to database"""

import pandas as pd
from cliuniapp.user import User
from cliuniapp import STUDENT_DB, SUBJECT_DB
import json


class StudentCheck:
    def __init__(self, student: User):
        self.student = student

    def read_db(self):
        """read student database"""
        with open(STUDENT_DB, "r") as file:
            student_file = json.load(file)
            student_db = pd.DataFrame(student_file)
            return student_db

    def check_student_exist(self):
        """check if student in the database"""
        with open(STUDENT_DB, "r") as file:
            student_file = json.load(file)
            student_db = pd.DataFrame(student_file)
            email = self.student.email

            if email in student_db.values:
                return True
            else:
                return False

    def add_student(self):
        """add student to the database"""
        if self.check_student_exist():
            print("student already exists")
        else:
            student_db = self.read_db()
            new_record = self.student.to_dict()
            with open(STUDENT_DB, "w") as file:
                org = student_db.to_dict("records")
                org.append(new_record)
                json.dump(org, file)
                print("Student has been added to the database")

    def delete_student(self):
        """delete student from the database"""
        if not self.check_student_exist():
            print("student do not exist")
        else:
            student_db = self.read_db()
            with open(STUDENT_DB, "w") as file:
                result = student_db.loc[student_db.email != self.student.email]
                json.dump(result.to_dict("records"), file)
                print("Student has been deleted from the database")


class SubjectCheck(StudentCheck):
    def __init__(self, student: User):
        super().__init__(student)
        self.valid_class_list = [
            "English",
            "Accounting",
            "Math",
            "History",
            "Finance",
            "Art",
        ]

    def read_db(self):
        """read subject database"""
        with open(SUBJECT_DB, "r") as file:
            subject_file = json.load(file)
            subject_db = pd.DataFrame(subject_file)
            return subject_db

    def check_subject_exist(self, subject):
        """check if the subject exists"""
        if not self.check_student_exist():
            raise ValueError("student does not exist")
        subject_db = self.read_db()
        subject_list = subject_db.loc[
            (subject_db.subject == subject) & (subject_db.email == self.student.email)
        ]
        if subject_list.empty:
            return False
        else:
            return True

    def add_subject(self, subject: str):
        """add subject to the database"""
        if not self.check_student_exist():
            raise ValueError("student does not exist")
        if subject not in self.valid_class_list:
            raise ValueError("subject is not valid")

        if self.check_subject_exist(subject):
            raise ValueError("subject has already enrolled")
        subject_db = self.read_db()

        if subject_db.loc[subject_db.email == self.student.email].shape[0] >= 4:
            raise ValueError("Cannot enroll new subject, Maximum 4 subjects")

        new_record = {"email": self.student.email, "subject": subject}
        with open(SUBJECT_DB, "w") as file:
            org = subject_db.to_dict("records")
            org.append(new_record)
            json.dump(org, file)
            print("Subject has been added to the database")

    def delete_subject(self, subject: str):
        """delete subject from the database"""
        if not self.check_student_exist():
            raise ValueError("student does not exist")
        if subject not in self.valid_class_list:
            raise ValueError("subject is not valid")

        if not self.check_subject_exist(subject):
            raise ValueError("subject has not been enrolled")
        subject_db = self.read_db()
        subject_db = self.read_db()
        with open(SUBJECT_DB, "w") as file:
            result = subject_db.loc[
                ~(
                    (subject_db.email == self.student.email)
                    & (subject_db.subject == subject)
                )
            ]
            json.dump(result.to_dict("records"), file)
            print("Subject has been deleted from the database")
