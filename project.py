from statistics import mean as m

admins = {'Python': '@pass1234', 'Hank': '@hank001'}

studentDict = {
    'Kim': [45, 34, 97],
    'Hank': [88, 47, 87],
    'Joy': [45, 77, 37],
    'Mercy': [77, 77, 76],
    'Alpha': [34, 77, 93],
    'Main': [45, 70, 57],
    'Beta': [67, 77, 82]
}


def enterGrades():
    nameToEnter = input('Student Name: ')
    gradeToEnter = input('grade: ')

    if nameToEnter in studentDict:
        print('adding grade ...')
        studentDict[nameToEnter].append(int(gradeToEnter))
    else:
        print('Student does not exist')
    print(studentDict)


def remove():
    nameToRemove = input('Student Name to remove?: ')

    if nameToRemove in studentDict:
        print('Deleting ...')
        del studentDict[nameToRemove]
    print(studentDict)

def add_student():
    nameAdd = input('student name: ')
    gradeF = input('First grade: ')
    grade2 = input('Second grade: ')
    studentDict[nameAdd] = {
        gradeF, grade2,

    }
    print(studentDict)

def studentAvg():
    for eachStudent in studentDict:
        gradeList = studentDict[eachStudent]
        avgGrade = m(gradeList)

        print(eachStudent, 'has an average of: ', avgGrade)

def main():
    print("""
    Grading Made easier.
    
    [1] - Enter Grades
    [2] - Remove Student
    [3] - Add student
    [4] - Student average mean
    [5] - EXIT
    
    """)
    action = input('what would you like to do today? (Enter Number) ')

    if action == '1':
        enterGrades()
    elif action == '2':
        remove()
    elif action == '3':
        add_student()
    elif action == '4':
        studentAvg()
    elif action == '5':
        exit()
    else:
        print('no valid choice, try again')


login = input('Username: ')
passwrd = input('password: ')

if login in admins:
    if admins[login] == passwrd:
        print('welcome, ', login)
        while True:
            main()
    else:
        print('invalid password, kumbuka oyah')
else:
    print('Invalid username, are you a hacker? .💀')
