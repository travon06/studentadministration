from Student import Student

def main():
    student = Student(0, 'marvin', 'engelbrecht')
    print(student.grades)
    student.add_grades_to_subject('math', [1,2,3])
    student.add_grades_to_subject('math', [1,1,1])
    print(student.grades)
    
if __name__ == '__main__':
    main()