#4. Ask a user to enter 10 (user-defined) numbers. Store them in a list and use a for loop
#  to determine the following: • Number of positive numbers • Number of negative numbers •
#  Number of zeros • Number of even numbers • Number of odd numbers • Largest number • 
# Smallest number • Use if-elif-else wherever appropriate. • You must repeat the analysis 
# using a while loop.

#create a list to analysis number
num_list = []

#create a dictionary to store numbers
number_list = {
    "numbers": []
}

#create a list will store all set of entries
list = []

#create a dicttionary will store the number types we need

number_analysis = {

    "positive_numbers": 0,
    "negative_numbers": 0,
    "no_of_zeros": 0,
    "even_numbers": 0,
    "odd_numbers": 0,
    "Largest_number": 0,
    "Smallest_number": 0
}


#set exit by default no
exit = "no"

#lets continue loop until i exit yes

while exit != "yes":

    for i in range(10):

        number = int(input("Enter a number:"))
        number_list["numbers"].append(number)

        number_analysis["Largest_number"] = max(number_list["numbers"])
        number_analysis["Smallest_number"] = min(number_list["numbers"])

        if number > 0:
            number_analysis["positive_numbers"] += 1

        elif number<0:
            number_analysis["negative_numbers"] += 1

        elif number == 0:
            number_analysis["no_of_zeros"] += 1

        elif number % 2 == 0:
            number_analysis["even_numbers"] += 1

        elif number % 2 != 0:
            number_analysis["odd_numbers"] += 1   

    list.append(number_analysis)
    num_list.append(number_list["numbers"])


    exit = input("Do you want to exit? (yes/no): ")  

    if exit == "yes":
        break
    elif exit == "no":
        continue

print(num_list)
print("Number analysis for each set of 10 numbers:")

for analysis in list:
    
    print(analysis)              
