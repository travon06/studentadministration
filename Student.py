class Student():
    def __init__(self, id: int, surname: str, name: str) -> None:
        self.surname = surname
        self.name = name 
        self.grades = {}
        
    def add_grades_to_subject(self, subject: str, grades: dict):
        if subject not in self.grades:
            self.grades[subject] = []
        self.grades[subject].extend(grades)
        
    def calculate_subject_gpa(self, subject: str) -> float:
        if subject not in self.grades:
            return None
        else:
            gpa = 0
            total_grades_in_subject = 0
            
            for index, grade in enumerate(self.grades[subject]):
                total_grades_in_subject += 1
                gpa += grade
            
            gpa /= total_grades_in_subject
            return gpa
        
if __name__ == '__main__':
    test = Student(0, 'surname', 'name')
    test.grades['math'] = [1,2,3,4,4,4,5]
    print(test.calculate_subject_gpa('math'))