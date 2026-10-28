class Students:
    students_names=""
    teacher_name=""
    number_of_students=14

    def __init__(self):
        print("Running constructor")
    def ask_for_name(self):
        self.students_name=input("What's the students name?")
        if self.students_name=="":
            print("Please enter a valid name")
        else:
            print(self.students_name)
        self.teacher_name=input("What's the teacher's name?")
        if self.teacher_name=="":
            print("Please enter a valid name")
        else:
            print(self.teacher_name)
    def show_details(self):
        print(self.students_name, "\n\n", self.teacher_name, "\n\n", self.number_of_students)
Margot=Students()
Pauline=Students()
Margot.ask_for_name()
Pauline.ask_for_name()
Margot.show_details()
Pauline.show_details()