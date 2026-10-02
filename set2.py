#Develop an electricity billing program. Ask the user for the number of units consumed and
#  calculate the bill according to: Units Rate 0-50 Rs. 2/unit 51-100 Rs. 3/unit 101-150 Rs. 
# 5/unit 151-200 Rs. 6/unit 201 and above Rs. 8/unit The program should have the following
#  features: • Use if-elif-else for the tariff. • Allow multiple customers to enter their 
# consumption using a while loop. • Store all bills in a list. • Use a for loop to display 
# all bills. • Calculate the total revenue collected. • Youcanusethefollowing concepts: 
# while, for, if-elif-else, list, arithmetic.

#create a dictionary to store user info

user_bill ={
    "name":"",
    "units": 0,
    "total_bill": 0
}

#create list to store users bill

list = []
exit = "no"

#this is for repeatitive asking user to enter more entries or not

while exit != "yes":

    user_bill["name"] = input("enter your name: ")
    user_bill["units"] = int(input("enter no of units you consumed: "))

    

    exit = input("do you want to exit then say yes or no: ")
    #set billing conditions


    if user_bill["units"] >=0 and user_bill["units"] <=50:

        user_bill["total_bill"] = user_bill["units"] * 2
        print("your total bill is: ", user_bill["total_bill"], "Rs")

    elif user_bill["units"] >=51 and user_bill["units"] <=100:

        user_bill["total_bill"] = 100+ ((user_bill["units"]-50)*3)
        print("your total bill is: ", user_bill["total_bill"] , "Rs")

    elif user_bill["units"] >=101 and user_bill["units"] <=150:

        user_bill["total_bill"] = 250+ ((user_bill["units"]-100)*5)
        print("your total bill is: ", user_bill["total_bill"] , "Rs")    

    elif user_bill["units"] >=151 and user_bill["units"] <=200:

        user_bill["total_bill"] = 500+ ((user_bill["units"]-150)*6)
        print("your total bill is: ", user_bill["total_bill"] , "Rs")
        
    elif user_bill["units"] >=201:

        user_bill["total_bill"] = 800+ ((user_bill["units"]-200)*8)
        print("your total bill is: ", user_bill["total_bill"] , "Rs")    

    list.append(user_bill["total_bill"]) #just to stor total bills of user




for bill in list:
    print("list of bills of each consumers: ", bill)

#print total revenue for all users

print("Total revenue collected: ", sum(list), "Rs")

   

    


