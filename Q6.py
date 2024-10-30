class College:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

    def display_college_data(self):
        return f"College Name: {self.name}\nAddress: {self.address}\nPhone: {self.phone}"

    def modify_college_data(self, name=None, address=None, phone=None):
        if name:
            self.name = name
        if address:
            self.address = address
        if phone:
            self.phone = phone


class Hostel:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def display_hostel_data(self):
        return f"Hostel Name: {self.name}\nAddress: {self.address}"

    def modify_hostel_data(self, name=None, address=None):
        if name:
            self.name = name
        if address:
            self.address = address


class Student(College, Hostel):
    def __init__(self, student_name, student_address, student_email, college_name, college_address, hostel_name, hostel_address):
        # Initialize College and Hostel
        College.__init__(self, college_name, college_address, phone="N/A")
        Hostel.__init__(self, hostel_name, hostel_address)
        
        # Student-specific attributes
        self.student_name = student_name
        self.student_address = student_address
        self.student_email = student_email

    def display_data(self):
        college_info = self.display_college_data()
        hostel_info = self.display_hostel_data()
        return (f"Student Name: {self.student_name}\n"
                f"Address: {self.student_address}\n"
                f"Email: {self.student_email}\n"
                f"{college_info}\n"
                f"{hostel_info}")

    def modify_college_data(self, name=None, address=None, phone=None):
        super(College, self).modify_college_data(name, address, phone)  # Call College's modify method


def main():
    college = None
    hostel = None
    student = None

    while True:
        print("\nMenu:")
        print("1. Create College")
        print("2. Create Hostel")
        print("3. Create Student")
        print("4. Display College Data")
        print("5. Display Hostel Data")
        print("6. Display Student Data")
        print("7. Modify College Data")
        print("8. Modify Hostel Data")
        print("9. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            college_name = input("Enter college name: ")
            college_address = input("Enter college address: ")
            college_phone = input("Enter college phone: ")
            college = College(college_name, college_address, college_phone)
            print("College created successfully.")

        elif choice == "2":
            hostel_name = input("Enter hostel name: ")
            hostel_address = input("Enter hostel address: ")
            hostel = Hostel(hostel_name, hostel_address)
            print("Hostel created successfully.")

        elif choice == "3":
            if college and hostel:  # Ensure college and hostel are created
                student_name = input("Enter student name: ")
                student_address = input("Enter student address: ")
                student_email = input("Enter student email: ")
                student = Student(student_name, student_address, student_email, college.name, college.address, hostel.name, hostel.address)
                print("Student created successfully.")
            else:
                print("Please create a college and hostel first.")

        elif choice == "4":
            if college:
                print("\nCollege Data:")
                print(college.display_college_data())
            else:
                print("College not created.")

        elif choice == "5":
            if hostel:
                print("\nHostel Data:")
                print(hostel.display_hostel_data())
            else:
                print("Hostel not created.")

        elif choice == "6":
            if student:
                print("\nStudent Data:")
                print(student.display_data())
            else:
                print("Student not created.")

        elif choice == "7":
            if college:
                new_name = input("Enter new college name (leave blank for no change): ")
                new_address = input("Enter new college address (leave blank for no change): ")
                new_phone = input("Enter new college phone (leave blank for no change): ")
                college.modify_college_data(new_name if new_name else None,
                                             new_address if new_address else None,
                                             new_phone if new_phone else None)
                print("College data modified successfully.")
            else:
                print("College not created.")

        elif choice == "8":
            if hostel:
                new_name = input("Enter new hostel name (leave blank for no change): ")
                new_address = input("Enter new hostel address (leave blank for no change): ")
                hostel.modify_hostel_data(new_name if new_name else None,
                                           new_address if new_address else None)
                print("Hostel data modified successfully.")
            else:
                print("Hostel not created.")

        elif choice == "9":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
