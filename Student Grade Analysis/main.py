#Import random function
import random

#main function
def main():
    gradeArray = []
    selection = 0

    for i in range(0, 50):
        grade = random.randint(0,100)
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
                grade = random.randint(0,99)
                gradeArray.append(grade)
            for grade in gradeArray:
                print (grade)
        if selection == "3":
           max_grade = max(gradeArray)
           min_grade = min(gradeArray)
           ave_grade = sum(gradeArray) / len(gradeArray)
           print ("The highest grade was " + str(max_grade) + "%")
           print ("The lowest grade was " + str(min_grade) + "%")
           print ("The average grade was " + str(ave_grade) + "%")
        if selection == "4":
            honours = 0
            for i in range(0, 50):
                if gradeArray[i] >= 80:
                    honours += 1
            print ("Total amount of honour students: " + str(honours))
        if selection == "5":
            print ("Program Closed.")
            quit()  
main() 