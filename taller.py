class student:
    def __init__(self, id: int, name: str):
        self.id: int = id
        self.name: str = name
        self.grades: list[float] = []
        self.is_passed: bool = False
        self.honor: bool = False

    def add_grades(self, g: float):
        if not (isinstance(g, (int, float))) and (0 <= g <= 100):
            return
        self.grades.append(g)
        print("Added grade: %s" % g)

    def calc_average(self):
        t = 0
        for x in self.grades:
            t += x
        avg = t / len(self.grades)
        return avg

    def check_honor(self):
        if self.calc_average() > 90:
            self.honor = True
    
    def get_letter(self):
        avg = self.calc_average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"
    
    def is_passed(self):
        avg = self.calc_average()
        self.is_passed = avg >= 60
        return self.is_passed
    

    def delete_grade(self, index: int = None, g: float = 0):
        if g not in self.grades and index is None:
            print("Grade not found: %s" % g)
            return
        if index is not None:
            if index < 0 or index >= len(self.grades):
                print("Index out of range: %s" % index)
            return
        if g in self.grades:
            self.grades.remove(g)
            print("Deleted grade: %s" % g)
            return
        if index is not None:
            print("Deleted grade %s at index: %s" % (self.grades[index], index))
            del self.grades[index]

    def report(self):
        print("Student ID: %s" % self.id)
        print("Student Name: %s" % self.name)
        print("Number of grades: %s" % len(self.grades))
        print("Average Grade = %s" % self.calc_average())
        print("Final Grade = %s" % self.get_letter())
        print("Passed = %s" % self.is_passed())
        print("Honor = %s" % self.honor)




def startrun():
    a = student(1, "John Doe")
    a.add_grades(100)
    a.add_grades(90)
    a.report()


startrun()
