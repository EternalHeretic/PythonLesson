
grades = [[5, 3, 3, 5, 4],
          [2, 2, 2, 3],
          [4, 5, 5, 2],
          [4, 4, 3],
          [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#20 / 5 = 4
#9 / 4 = 2.25
#16 / 4 = 4
#11 / 3 = 3.66
#24 / 5 = 4.8

grades_m =  []
for i in grades:
    avg_grades = sum(i)/len(i)
    grades_m.append(avg_grades)

student = sorted(students)
students_grades = dict(zip(student, grades_m))
print(students_grades)
