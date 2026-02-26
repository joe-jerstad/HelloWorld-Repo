def min_grade(exams):
    grade_min = 100

    for course in exams:
        if exams[course] < grade_min:
            grade_min = exams[course]
            worst_grade = course

    return worst_grade

test_1 = {'Physics' : 82, 'Math' : 65, 'History' : 75, 'Biology' : 95, 'English' : 87}
test_2 = {'Chemistry' : 78, 'Algebra' : 88, 'History' : 72, 'Geography' : 85}

print(min_grade(test_2))