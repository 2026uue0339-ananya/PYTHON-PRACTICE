#6. Develop a complete Smart College Canteen Management System.You should clearly define 
# the scope and consideration of your development (open to your thought process). 
# Think about the application the way you would like to use it with different 
# options/features.


#my food item list

foods = {
    "momos": {"price": 45, "quantity": 30},
    "chowmin": {"price": 75, "quantity": 70},
    "coldrink": {"price": 35, "quantity": 20},
    "chips": {"price": 20, "quantity": 120},
    "pizza": {"price": 80, "quantity": 34}
}


total_bill = 0
total_no = 0

print(foods)
print("select foods to your wish list")

snacks = ""
cart = []

print("type 'done' when you finish your shopping")

#to allow to add multiple food in the cart

while snacks!= "done":

    snacks =input("choose whatever you want: ")
   
    if snacks in foods:     
            
        number = int(input(f"No of {snacks} you want: "))
        
        cart.append(snacks)

        #calculate total bill

        total_bill += sum(number * foods[product]["price"] for product in cart)

    elif snacks == "done":
        
        break    

    else:
        print("Sorry, item not found!")    #run  process if food avaiable  

    
   #show the wishlist
    
print("Your added to your cart: ",cart)

#show the bill

print("you have to pay ", total_bill, " Rs.")

print("Thank you for shopping!!")
    
                