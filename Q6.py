class College:
    def __init__(self, college_name, college_address, college_phone):
        self.college_name = college_name  # College name
        self.college_address = college_address  # College address
        self.college_phone = college_phone  # College phone

    def display(self):
        print(f"College Name: {self.college_name}")
        print(f"College Address: {self.college_address}")
        print(f"College Phone: {self.college_phone}")

    def modify(self, college_name=None, college_address=None, college_phone=None):
        if college_name:
            self.college_name = college_name
        if college_address:
            self.college_address = college_address
        if college_phone:
            self.college_phone = college_phone


class Hostel:
    def __init__(self, hostel_name, hostel_address):
        self.hostel_name = hostel_name  
        self.hostel_address = hostel_address  

    def display(self):
        print(f"Hostel Name: {self.hostel_name}")
        print(f"Hostel Address: {self.hostel_address}")

    def modify(self, hostel_name=None, hostel_address=None):
        if hostel_name:
            self.hostel_name = hostel_name
        if hostel_address:
            self.hostel_address = hostel_address


class Student(College, Hostel):
    def __init__(self, student_name, student_address, student_phone, email, college_name, college_address, college_phone, hostel_name, hostel_address):
        College.__init__(self, college_name, college_address, college_phone)
        Hostel.__init__(self, hostel_name, hostel_address)
        self.student_name = student_name  
        self.student_address = student_address  
        self.student_phone = student_phone 
        self.email = email  

    def display(self):
        print("Student Details:")
        print(f"Name: {self.student_name}")
        print(f"Address: {self.student_address}")
        print(f"Phone: {self.student_phone}")
        print(f"Email: {self.email}")
        
        print("\nCollege Details:")
        College.display(self)  
        
        print("\nHostel Details:")
        Hostel.display(self) 
    def modify_college(self, college_name=None, college_address=None, college_phone=None):
        College.modify(self, college_name=college_name, college_address=college_address, college_phone=college_phone)

    def modify_hostel(self, hostel_name=None, hostel_address=None):
        Hostel.modify(self, hostel_name=hostel_name, hostel_address=hostel_address)


student = Student(
    student_name="Vishwajeet",
    student_address="Pune",
    student_phone="1234567890",
    email="abc@xyz.com",
    college_name="MIT College",
    college_address="Alandi",
    college_phone="9876543210",
    hostel_name="ABC Hostel",
    hostel_address="Pimpri"
)

student.display()
student.modify_college(college_name="PCCOE College", college_address="Near Pune", college_phone="1234567891")
student.modify_hostel(hostel_name="XYZ Hostel", hostel_address="Dapodi")
print("\nUpdated Student Details:")
student.display()
