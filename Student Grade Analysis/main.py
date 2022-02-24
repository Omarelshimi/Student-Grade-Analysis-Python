#Import random function
import math
import random
from re import I



#main function
def main():
    gradeArray = []
    selection = 0
    max = gradeArray[i]

    for i in range(0, 50):
        grade = random.randint(0,101)
        gradeArray.append(grade)

    while selection != 5:
        print(f'''
        Main Menu
            1. Display All Grades
            2. Randomize Grades
            3. Stats
            4. Count Honours
            5. Exit
            ''')
        selection = input("Type a number corresponding with it's option please: ") 
        if selection == "1":
            for grade in gradeArray:
                print (grade)
        if selection == "2":
            gradeArray.clear()
            for i in range(0, 50):
                grade = random.randint(0,101)
                gradeArray.append(grade)
            for grade in gradeArray:
                print (grade)
        if selection == "3":
            for i in range(0, len(gradeArray)):
                if (gradeArray[i] > max):
                    max = gradeArray[i]
            print ("The highest grade was" + max) 
main()