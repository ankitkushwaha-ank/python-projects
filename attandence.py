# **** attendance marking script ****
import json
import os
import datetime


class IITPATNA:
    college_name = "Indian Institute of Technology Patna"
    student_file = "students.json"

    def __init__(self, student_name=None, roll_no=None, registration_no=None, batch=None, semester=None,
                 **student_info):
        self.student_name = student_name
        self.roll_no = roll_no
        self.registration_no = registration_no
        self.batch = batch
        self.semester = semester
        self.student_info = student_info

    @staticmethod
    def load_students():
        if os.path.exists(IITPATNA.student_file):
            with open(IITPATNA.student_file, "r") as file:
                return json.load(file)
        return {}

    @staticmethod
    def save_students(students):
        with open(IITPATNA.student_file, "w") as file:
            json.dump(students, file, indent=4)

    def register_student(self):
        students = self.load_students()
        if self.roll_no in students:
            print("Student already registered!")
            return

        students[self.roll_no] = {
            "name": self.student_name,
            "registration_no": self.registration_no,
            "batch": self.batch,
            "semester": self.semester,
            "additional_info": self.student_info
        }

        self.save_students(students)
        print(f"Student {self.student_name} registered successfully!")

    @classmethod
    def student_login(cls):
        roll_no = input("Enter your Roll No.: ")
        students = cls.load_students()

        if roll_no in students:
            student_data = students[roll_no]
            print(f"\nWelcome {student_data['name']} to IIT Patna!")
            print(f"Roll No.: {roll_no}")
            print(f"Registration No.: {student_data['registration_no']}")
            print(f"Batch: {student_data['batch']}")
            print(f"Semester: {student_data['semester']}")
        else:
            print("Student not found! Please register first.")

    @classmethod
    def mark_attendance(cls):
        roll_no = input("Enter your Roll No. to mark attendance: ")
        students = cls.load_students()

        if roll_no in students:
            time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"Attendance marked for {students[roll_no]['name']} at {time_now}")
        else:
            print("Student not found! Please register first.")


#lets play your code in loop  \ if you have to impplement it in your website simply you remove this part and add some flask APIs :)
while True:
    print("\n1. Register Student")
    print("2. Student Login")
    print("3. Mark Attendance")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter your name: ")
        roll_no = input("Enter your Roll No.: ")
        # reg_no = input("Enter your Registration No.: ")
        batch = input("Enter your Batch: ")
        semester = input("Enter your Semester: ")
        # additional_info = {"mobile": input("Enter your Mobile No.: "), "address": input("Enter your Address: ")}

        student = IITPATNA(name, roll_no, batch, semester) #if you want to add reg_no or additional_info simply add in this line :)
        student.register_student()
    elif choice == "2":
        IITPATNA.student_login()
    elif choice == "3":
        IITPATNA.mark_attendance()
    elif choice == "4":
        break
    else:
        print("Invalid choice! Try again.")
