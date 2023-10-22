from pathlib import Path

PACKAGE_DIR = Path(__file__).parent.parent
STUDENT_DB = Path(PACKAGE_DIR / "data/students.data")
SUBJECT_LIST = ["0100","0101","0102","0103","0104","0105","0106"]
GRADE = {'F':[25,49],'P':[50,59],'C':[60,69],'D':[70,79],'HD':[80,100]}