class Student():
    def __init__(self, id: int, surname: str, name: str) -> None:
        self.surname: str = surname
        self.name: str = name 
        self.grades: dict = {}
        
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
                        
            for grade in self.grades[subject]:
                total_grades_in_subject += 1
                gpa += grade
            
            gpa /= total_grades_in_subject
            return gpa
        
    def calculate_gpa_for_all(self) -> dict:
        grades_with_gpa = {}
        
        total_grades_in_grades = 0
        sum_of_all_grades = 0
        
        for subject in self.grades:
            
            total_grades_in_subject = 0
            sum_of_grades_in_subject = 0
            
            for grade in self.grades[subject]:
                total_grades_in_grades += 1
                total_grades_in_subject += 1
                
                sum_of_grades_in_subject += grade
                sum_of_all_grades += grade
            
            subject_gpa = sum_of_grades_in_subject / total_grades_in_subject
            grades_with_gpa[subject] = subject_gpa
            
        overall_gpa = sum_of_all_grades / total_grades_in_grades
        grades_with_gpa['Averrage'] = overall_gpa
        
        return grades_with_gpa
            
if __name__ == '__main__':  
    test_student = Student(0, 'Surname', 'name')
    test_student.add_grades_to_subject('math', [1,2])
    test_student.add_grades_to_subject('english', [2,2])
    test_student.add_grades_to_subject('history', [1])
    
    print(test_student.calculate_gpa_for_all())
