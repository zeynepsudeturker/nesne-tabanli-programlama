# Person sınıfı
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"

# Student sınıfı (Person sınıfından türetilmiş)
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    
    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Student ID: {self.student_id}"

# Teacher sınıfı (Person sınıfından türetilmiş)
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    
    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Subject: {self.subject}"

# Örnek kullanım
if __name__ == "__main__":
    person = Person("Ahmet", 30)
    student = Student("Ayşe", 20, "S12345")
    teacher = Teacher("Mehmet", 40, "Matematik")
    
    print(person.display_info())
    print(student.display_info())
    print(teacher.display_info())
