# class definition
class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.ID = 0

def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student3 = Student()
    
    student1.name = "Dominic"
    student1.age = 19
    student1.ID = 5672325

    student2.name = "Olivia"
    student2.age = 21
    student2.ID = 235775

    student3.name = "Sofia"
    student3.age = 26
    student3.ID = 277775


    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name}, {student1.age} years old, ID: {student1.ID}')
    print(f'{student2.name}, {student2.age} years old, ID: {student2.ID}')
    print(f'{student3.name}, {student3.age} years old, ID: {student3.ID}')

if __name__ == "__main__":
    main()