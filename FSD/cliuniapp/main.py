from cliuniapp.user import User
from cliuniapp.database import StudentCheck, SubjectCheck

stephen = User(name="stephen", email="stephen@university.com", password="xxxxxx")
ian = User(name="Zhijia Guo", email="zhijia.guo@university.com", password="password3")


SubjectCheck(ian).add_subject("Accounting")
