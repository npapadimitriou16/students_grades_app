grades = []

def addgrades(grade):
    grades.append(grade)

def average():
    if len(grades) == 0:
        return 0
    
print("This is a grade manager")