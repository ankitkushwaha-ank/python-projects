from tkinter.font import names


class Student:
    university = "Indian institute of technology"

    def __init__(self ,name, roll, session, sem, batch):
        self.name  = name
        self.roll_number = roll
        self.session = session
        self.semester = sem
        self.Batch =  batch

    def student_info(self):
        print(f'student name is {self.name}')
        print(f'  Roll no. - {self.roll_number}')
        print(f'  session - {self.session}')
        print(f'  Semester - {self.semester}')
        print(f'  Batch - {self.Batch}')
        print("Indian institute of technology patna")

    #if the sem change
    def chnage_sem(self , current_sem):
        self.new_sem = current_sem
        print(f'student is in {self.new_sem} semester')

std1 = Student("Ankit kushwaha" , "12res24a840" , "2023-27" , 1 ,2)
std2 = Student("Ayushi kumari" , "12res24a854" , "2023-27" , 1,2)
std3 = Student("Imdad akram" , "12res24a860" , "2023-27" , 1,2)
std4 = Student("Saurav kumar" , "12res24a920" , "2023-27" , 1,2)
std5 = Student("Adarsh kushwaha" , "12res24a210" , "2023-27" , 1,1)

print("---------------------------------")
std1.student_info()
std1.chnage_sem(2)

std1.student_info()
# std1.__init__('harsh kumar' , "12res24a876", "23-27" , "2")
print("---------------------------------")
std2.student_info()
print("---------------------------------")
std3.student_info()
print("---------------------------------")
std4.student_info()
print("---------------------------------")
std5.student_info()
print("---------------------------------")
