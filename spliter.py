# I gonna make a bill spliter app
# This app will help you split bills among friends or family members
# First a message of welcome to the restaurant will be displayed
# Then the user will be prompted to enter the total bill amount
# After that, the user will be asked if the want to split the bill or not
# if they say no, we will display the total bill amount and exit the program
# if they say yes, we will ask them how many people are splitting the bill
# we will ensure that the number of people is greater than 0 and is an integer


def main():
    #printer welcome message to the user in bold
    BOLD = '\033[1m'
    END = '\033[0m'
    welcome= "Welcome to sprite restaurant bar and grill".upper()
    print(BOLD + welcome + END)
    # bill_total= float(input("Please enter the total bill amount :"))
    print()
    while True: 
        try:
             #ensuring that the user's inout is a float
            number =  float(input("PLEASE ENTER THE BILL AMOUNT").upper())
            print()
            #ensuring that the number enter is positive
            if number > 0 :
                bill_total = number 
                break
            else :
             #message error if the number is negative
             print("Sorry, The Number need to be more than 0$")
             print()
             #if input is not a number, display a error message
        except ValueError :
             print("invalid input.")
             print()

    while True:
        #getting the user's choice and covert all answer to lowercase and delete any space: YeS=yes
        split_bill= input("do you want to split the bill?(yes/no)").lower().strip()
        #if the user's choice is yes or no
        if split_bill in ("yes" , "no"):
            break
        else:
            #if the user's choice is not yes or no, display a error message
            print("Invalid entry. please enter yes or no.")
            print()
            #if user says no, give them the total amount of bill
    if split_bill == "no":
        print()
        print(f"the total amount is : $" , bill_total)
        print()
        #if user says yes, ask them to put the amount of people that is sharing the bill and do the math
    if split_bill == "yes" :
        while True:
            try:
                group_number=int(input("How many people are sharing: "))
                if group_number > 0:
                    split_number = bill_total / group_number
                    print()
                    print("The total amount for each person is : $" , round(split_number , 2))
                    break
                else:
                    print("Invalid entry, enter a positive number")
            except ValueError:
                print("invalid enter")

            
main()