subjects = ["Algorithms", "Software Design", "Poetry", "Electronics"]
grades = ["98", "88", "85", "90"]
gradebook = zip(subjects, grades)
print("Course  ", "  Score")
for subject, grade in zip(subjects, grades):
    print(subject, '\t', grade)
print('\n')
grade_book = list(gradebook)
grade_book.append(['computer science', 100])
grade_book.append(['virtual Arts', 93])
grade_book[5][1] += 5
grade_book.remove(grade_book[2])
#grade_book[2].remove(85)
#grade_book[2].append('Passed')
grade_book.append(grade_book['Poetry', 'Passed'])
print("Course  ", "   Score")
for subject, grade in grade_book:
    print(subject, '\t', grade)
print('\n')

subjects2 = ["Calculus", "OOP", "Cyber Security", "Physics"]
grades2 = ["94", "80", "82", "70"]
last_semester_gradebook = zip(subjects2, grades2)
last_gradebook = list(last_semester_gradebook)
full_gradebook = list(grade_book + last_gradebook)
print("Course  ", "   Score")
for subject, grade in full_gradebook:
    print(subject, '\t', grade)

