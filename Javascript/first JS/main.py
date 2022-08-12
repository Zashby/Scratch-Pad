

def grade():
    while True:

        grade = int(input('Enter your grade: '))
        if grade in range(0,101):
            break
        else:
            continue
    letter_grade = ''
    if grade >= 90:
        letter_grade = 'A'
    elif grade >= 80:
        letter_grade = 'B'
    elif grade >= 70:
        letter_grade = 'C'
    elif grade >= 60:
        letter_grade = 'D'
    else:
        letter_grade = 'F'

    return f'Your grade is a {letter_grade}'


print(grade())