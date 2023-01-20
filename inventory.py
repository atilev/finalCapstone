#=====importing libraries===========
import os #for clearing the screen
from time import sleep #for setting delay

#====Format Section====
UNDERLINE = "\033[4m"
BOLD = "\033[1m"
RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[33m"

#========The beginning of the class==========
class Shoe:
    #constructor setting
    def __init__(self, country, code, product, cost, quantity):
        #initialising attributes:
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
    
    #return the cost of the shoe in this method
    def get_cost(self):
        return self.cost
    
    #return the quantity of the shoes.
    def get_quantity(self):
        return self.quantity
 
    #returns a string representation of a class
    def __str__(self):
        return f"{self.country:<20} ■ {self.code:<10} ■ {self.product:<25} ■ {self.cost:<10} ■ {self.quantity:<10}"

#=============Shoe list===========
'''The list will be used to store a list of objects of shoes.'''
shoe_list = []

#==========Functions outside the class==============
def read_shoes_data():
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''  
    while True:

        #try & expect to handle file errors
        try:
            #as terminal cannot be cleared properly, when we got more then a page info > printing 1000 empty lines
            print("\n"*1000)
            #clearing the screen.
            os.system("cls")
            print(f"{BOLD}{UNDERLINE}Read the data from a file{RESET}\n")
            file_name = input("Please enter your file name: ").lower()
            file = open(file_name, "r")
            #read from second row
            next(file)

            #for loop to read the lines from the file
            for line in file:
                #split each line to a temp_store list
                temp_store = line.strip().split(",")
                #creating a temp_shoe object
                temp_shoe = Shoe(temp_store[0],temp_store[1],temp_store[2],temp_store[3],temp_store[4])
                #adding temp shoe to the shoe list store
                shoe_list.append(temp_shoe)
            print(f"{GREEN}inventory.txt file has been successfully loaded.{RESET}")
            #closing the file
            file.close()
            sleep(2) #2 sec delay to read the last message
            break

        #expect to handle IOEerrors
        except IOError:
            print(f"{RED}Your file is not available to read. Make sure file name correct and it is in the right folder{RESET}")
            next_step = input(f"{YELLOW}Press enter to try to read again{RESET} or {BLUE}(m) to go back to the main menu: {RESET}").lower()
            if next_step == "m":
                return
            else:
                continue
        
#create a new shoe object and add to the list
def capture_shoes():
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    while True:
        #as terminal cannot be cleared properly, when we got more then a page info > printing 1000 empty lines
        print("\n"*1000)
        #clearing the screen.
        os.system("cls")
        print(f"{BOLD}{UNDERLINE}Adding a new shoe to the store{RESET}\nPlease enter the following data:") 
        country = input("Country: ")
        code = input("Code: ")
        product = input("Product: ")
        cost = input("Cost: ")
        quantity = input("Quantity: ")

        #if else error handling if empty fields entered
        if country == "" or code == "" or product == "" or cost == "" or quantity == "":
            print(f"{RED}Datafileds cannot be empty.{RESET}")
            next_step = input(f"{YELLOW}Press enter to try again{RESET} or {BLUE}(m) to go back to the main menu: {RESET}").lower()
            if next_step == "m":
                return
            else:
                continue
        
        #Try except to handle if not number entered for Cost and quantity 
        try:
            int(cost) 
            int(quantity)
            break
        except ValueError:
            print(f"{RED}Cost and quantity have to be whole number.{RESET}")
            next_step = input(f"{YELLOW}Press enter to try again{RESET} or {BLUE}(m) to go back to the main menu: {RESET}").lower()
            if next_step == "m":
                return
            
    #creating new_email object
    new_shoe = Shoe(country, code, product, cost, quantity)
    # Now add the email to the Inbox
    shoe_list.append(new_shoe)
    # Print a success message
    print(f"{GREEN}Shoe has been added to the store database.{RESET}")
    sleep(2) #2 sec delay to read the last message

def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    show all emails'''
    print("\n"*1000)
    os.system("cls")

    #error handling if shoe store is empty
    if shoe_list == []:
        print(f"{RED}Store is empty, please add products.{RESET}")
        sleep(2) #2 sec delay to read the last message
        return
    else:
        print(f"{BOLD}{UNDERLINE}View all shoes{RESET}\n") 
        print(f"\n      Country        █    Code    █           Product         █    Cost    █ Quantity")
        print(f"{GREEN}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{RESET}")
        
        for i in shoe_list:
            print(i)
            print(f"{BLUE}---------------------------------------------------------------------------------------{RESET}")
        
        print(f"{GREEN}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{RESET}")
        input(f"{BLUE}Press enter to return to the main menu{RESET}")

#Product with lowest stock (Re-stock)
def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    print("\n"*1000)
    os.system("cls")
    qty = []
    
    #error handling if shoe store is empty
    if shoe_list == []:
        print(f"{RED}Store is empty, please add products.{RESET}")
        sleep(2) #2 sec delay to read the last message
        return
    else:
        print(f"{BOLD}{UNDERLINE}Product with lowest stock (Re-stock){RESET}\n") 
        #for loop to load the quantity into qty list and find the index of the min value
        
        for i in shoe_list:
            qty.append(int(i.quantity))
        
        min_qty = min(qty)
        min_qty_index = qty.index(min_qty)

        #printing lowest stock item
        print(f"      Country        █    Code    █           Product         █    Cost    █ Quantity")
        print(f"{GREEN}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{RESET}")
        print(shoe_list[min_qty_index])
        print(f"{GREEN}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{RESET}")

        next_step = input(f"{YELLOW}To re-stock enter (r){RESET} or {BLUE}press enter to go back to the main menu: {RESET}").lower()
        
        if next_step == "r":
            #"while try except" to handle value error for number input  
            while True:
                try:
                    increase_qty = int(input("Please enter the quantity to increase the stock: "))
                    break
                except ValueError:
                    print(f"{RED}Wrong entry, please enter a number{RESET}")
            
            #calculating the new quantity
            new_qty = min_qty + increase_qty
            #updating the quantity of the object in the list
            shoe_list[min_qty_index].quantity = new_qty
            print("\n"*1000)
            os.system("cls")
            #printing the updated quantity
            print(f"      Country        █    Code    █           Product         █    Cost    █ Quantity")
            print(f"{GREEN}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{RESET}")
            print(shoe_list[min_qty_index])
            print(f"{GREEN}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{RESET}")
            input(f"{GREEN}Shoe has been re-stocked.{BLUE}\n\nPress enter to return to the main menu{RESET}")
            return
        else:
            return

def seach_shoe():
    '''
    This function will search for a shoe from the list
    using the shoe code and return this object so that it will be printed.
    '''    
    print("\n"*1000)
    os.system("cls")
    code_list = []

    #error handling if shoe store is empty
    if shoe_list == []:
        print(f"{RED}Store is empty, please add products.{RESET}")
        sleep(2) #2 sec delay to read the last message
        return
    else:
        #for loop to load the codes into the code_list list and find the entered code
        for i in shoe_list:
            code_list.append(i.code)
        
        #"while try except" to handle value error is the sku is not in the list
        while True:
            try:
                print("\n"*1000)
                os.system("cls")
                print(f"{BOLD}{UNDERLINE}Product finder by SKU code{RESET}\n") 
                requested_code = input("Please enter the SKU code to look up the product: ")
                #finding the index of the requested sku code
                requested_index = code_list.index(requested_code)
                #printing the requested product
                print(f"\n      Country        █    Code    █           Product         █    Cost    █ Quantity")
                print(f"{GREEN}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{RESET}")
                print(shoe_list[requested_index])
                print(f"{GREEN}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{RESET}")
                input(f"{BLUE}Press enter to return to the main menu{RESET}")
                break
            except ValueError:
                print(f"{RED}SKU code is not in the database.{RESET}")
                next_step = input(f"{YELLOW}Press enter to try another code{RESET} or {BLUE}(m) to go back to the main menu: {RESET}").lower()
                if next_step == "m":
                    return
                else:
                    continue

def value_per_item():
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    print("\n"*1000)
    os.system("cls")

    #error handling if shoe store is empty
    if shoe_list == []:
        print(f"{RED}Store is empty, please add products.{RESET}")
        sleep(2) #2 sec delay to read the last message
        return
    else:
        print(f"{BOLD}{UNDERLINE}Products value & Total value{RESET}\n") 
        total = 0
        print(f"      Country        █    Code    █           Product         █    Cost    █  Quantity  █ Value")
        print(f"{GREEN}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{RESET}")
        
        for i in shoe_list:
            #getting cost and quantity using the class functions
            value = int(i.get_cost()) * int(i.get_quantity())
            #calculating to total stock value
            total += value
            print(f"{i} ■ ${value}")
            print(f"{BLUE}------------------------------------------------------------------------------------------------------{RESET}")
        print(f"{GREEN}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{RESET}")
        print(f"{YELLOW}The Total stock value: {BOLD}${total}{RESET}")
        input(f"{BLUE}Press enter to return to the main menu{RESET}")

#Product with highest stock (being for sale).
def highest_qty():
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    print("\n"*1000)
    os.system("cls")
    qty = []
    
    #error handling if shoe store is empty
    if shoe_list == []:
        print(f"{RED}Store is empty, please add products.{RESET}")
        sleep(2) #2 sec delay to read the last message
        return
    else:
        print(f"{BOLD}{UNDERLINE}Product with highest stock (being for sale){RESET}\n") 

        #for loop to load the quantity into qty list and find the index of the min value
        for i in shoe_list:
            qty.append(int(i.quantity))
        
        max_qty = max(qty)
        max_qty_index = qty.index(max_qty)

        #printing lowest stock item
        print(f"      Country        █    Code    █           Product         █    Cost    █ Quantity")
        print(f"{GREEN}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{RESET}")
        print(shoe_list[max_qty_index])
        print(f"{GREEN}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{RESET}")
        print(f"{YELLOW}{BOLD}This shoe as being for sale.{RESET}")
        input(f"{BLUE}Press enter to return to the main menu{RESET}")

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''

menu_options = f'''{GREEN}{BOLD}{UNDERLINE}
Welcome to the Nike Warehouse System! What would you like to do?
{RESET}
{BLUE}1{RESET} - Read the data from a file.
{BLUE}2{RESET} - Adding a new shoe to the store.
{BLUE}3{RESET} - View all shoes.
{BLUE}4{RESET} - Product with lowest stock (Re-stock).
{BLUE}5{RESET} - Product search by SKU code.
{BLUE}6{RESET} - Products value & Total value.
{BLUE}7{RESET} - Product with highest stock (being for sale).
{BLUE}8{RESET} - Exit this program.
'''

while True:
    #as terminal cannot be cleared properly, when we got more then a page info > printing 1000 empty lines
    print("\n"*1000)
    #clearing the screen.
    os.system("cls")
    user_choice = input(menu_options)
    
    #Read the data from a file.
    if user_choice == "1":
        read_shoes_data()

    #Adding a new shoe to the store.
    elif user_choice == "2":
        capture_shoes()
    
    #View all shoes.
    elif user_choice == "3":
        view_all()
        
    #Product with lowest stock (Re-stock)
    elif user_choice == "4":
        re_stock()
      
    #Product search by SKU code.
    elif user_choice == "5":
        seach_shoe()

    #Products value & Total value
    elif user_choice == "6":
        value_per_item()
    
    #Product with highest stock (being for sale)
    elif user_choice == "7":
        highest_qty()

    #exit this program
    elif user_choice == "8":
        print("\n"*1000)
        os.system("cls")
        print(f"{BLUE}Goodbye{RESET}")
        break

    else:
        print(f"{RED}Incorrect input, please try again{RESET}")
        sleep(2) #2 sec delay to read the last message