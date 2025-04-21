import datetime

class IITPATNA:
    college_name = "Indian institute of technology patna"

    def __init__(self,student,roll_no,registration_no,batch,semester,**student_info):
        self.student_name = student
        self.roll_no = roll_no
        self.registration_no = registration_no
        self.batch = batch
        self.semester = semester
        self.student_info = student_info

    def student_login(self):
        student = input('what is your name:-')
        self.name = student
        roll_no = input('enter your Roll no. :-')
        self.roll_no = roll_no
        reg_no = input('enter your registration number:-')
        self.reg_no = reg_no
        self.batch = input('in which batch you are? :-')
        self.semester = input('which semsetre you are:-')


    def logged_in(self):
        print(f'welcome {self.name} to iit patna')
        print(f'Roll no. - {self.reg_no}')
        print(f'Registration no. - {self.registration_no}')
        print(f'Batch - {self.batch}')
        print(f'Semester - {self.semester}')

    def college_login(self):
        print(f'welcome {self.student_name} to iit patna')
        print(f'Roll no. - {self.roll_no}')
        print(f'Registration no. - {self.registration_no}')
        print(f'Batch - {self.batch}')
        print(f'Semester - {self.semester}')

    def attendance(self):
        std = input('what is your name:- ')
        roll_no = input('roll no:- ')
        self.attend = std

        print(f'Today {self.attend} is present')



student = IITPATNA("Ankit kushwaha",854,
                   "12res24a854",2,2,
                   mobile =8092316838,adress = "bettiah, west champaran, bihar")
# student.student_login()
print("x"*20)
# student.college_login()
student.attendance()