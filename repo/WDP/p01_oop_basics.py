"""Practical 1: OOP basics - classes, objects, attributes and methods."""


class Student:
    college = "SLTIET Rajkot"          # class attribute (shared by all objects)

    def __init__(self, name, enrollment, marks):
        self.name = name                # instance attributes
        self.enrollment = enrollment
        self.marks = marks

    def average(self):                  # instance method
        return sum(self.marks) / len(self.marks)

    def grade(self):
        avg = self.average()
        if avg >= 75:
            return "Distinction"
        if avg >= 60:
            return "First Class"
        if avg >= 40:
            return "Pass"
        return "Fail"

    def display(self):
        print(f"Name       : {self.name}")
        print(f"Enrollment : {self.enrollment}")
        print(f"College    : {Student.college}")
        print(f"Marks      : {self.marks}")
        print(f"Average    : {self.average():.2f}")
        print(f"Grade      : {self.grade()}\n")

    def __str__(self):
        return f"Student({self.name}, {self.enrollment})"


if __name__ == "__main__":
    s1 = Student("Yash", "2301010001", [78, 82, 90])
    s2 = Student("Amit", "2301010002", [55, 48, 62])
    s1.display()
    s2.display()
    s2.marks.append(70)                 # modifying an attribute
    print("Updated average of", s2, "=", round(s2.average(), 2))
