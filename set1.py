#Write a Python program to store the marks of 5 (user-defined) students in a list. 
# The program should include the following features: • Accept marks from the user. 
# • Display all marks using a for loop. • Find the highest and lowest marks.
#  • Calculate the average. • Count the number of students who passed and failed using 
# if-else. • Use while to repeatedly ask whether the user wants to enter another set of
#  marks. • You can use the following concepts: list, for, while, if-else, max(), min(), 
# sum().

marks = []

passed = 0
failed = 0

val = ""

while val != "no": #to repeadtedly ask for entering marks
    for i in range(5): #in each set allow only 5 students to entr marks
        student_marks = int(input("Enter your marks: "))
        marks.append(student_marks)

        #writing pass -fail conditions

        if student_marks >= 50:
            passed += 1
        else:
            failed += 1

    val = input("Do you want to enter marks for another student? (yes/no): ")

    if val == "no":

        #printing required answers 

        print("Total students passed:", passed)
        print("Total students failed:", failed)
        print("Marks of all students:", marks)
        print("Average marks of all students:", sum(marks) / len(marks))
        print("Highest marks:", max(marks))
        print("Lowest marks:", min(marks))

        break

    elif val == "yes":
        continue

    else:
        #not allow to type anyother than yes or no

        print("Invalid input. Please enter 'yes' or 'no'.")
        val = input("Do you want to enter marks for another student? (yes/no): ")
        

