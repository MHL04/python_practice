# “Did you get paid or spend money?”
# If paid: ask how much income to add.
# If spent: ask what it was for, how much it cost, and its category.
# Ask whether they want to record another transaction.
# Show a summary: income this month, expenses today, expenses this month, and money left.




  class Expense:
    def __init__(self, amount,category):
        self.amount = amount
        self.category=category
    



print("EXPENSE TRACKER ")
print()

#Get the user paycheck, and make sure the user enter a number and not something else 
#with a loop that will keep asking till a correct entry
while True:
    try:
        income_record = float(input("HOW MUCH YOU'VE GOT PAID : "))
        break
    except ValueError:
        print("ENTER A NUMBER : ")

#Get Spending data, and ensure that user answer yes or no, with a loops that kepp asking
#till a good entry
while True:
    print()
    expense_record = input("Did you spend Money today: YES OR NO: ").strip().lower()
    if expense_record in ("yes", "no"):
        break
    print("ANSWER YES OR NO")
#creation of a empty list where the data will be store category and amount 
expenses = []

#loop to verify the user answer is yes and is  a number with isalpha() function to print an error message
money_left=income_record
if expense_record == "yes":
    while True:

        while True:
         
         category = input("Please enter the Category : ").strip().upper()
         if category.isalpha():
            break
         print("Please enter a category")

        
        #after the category,get the amount spent, and now add the categiry entry to the list and the amount associated using append
        
        while True:
            try:
                price = float(input(f"How much did you spend on {category}: "))
                
                if price > money_left:
                    
                    print("overdraft! Lower the mount")
                    continue
                expense_record=Expense(price,category)
                expenses.append(expense_record)
                money_left-=price
                break
            except ValueError:
                print("Enter a valid price")
        #ask for more expenses ,if answer is yes it breaks and come back to the top outerloopnto enter the category and price
        while True:
            more_expenses = input("Do you have any other expenses, YES/NO: ").strip().lower()
            if more_expenses in ("yes", "no"):
                break
            print("Please enter yes or no")

        if more_expenses == "no":
            break
    #create an empty dictionnary    and a loop that will create a line category and add the category enter by the user and price with the amount 
    #enter by the user 
    category_totals = {}
    for expense in expenses:
        category = expense.category
        amount = expense.amount
        #Add this expense's amount to whatever total that category already has — or start at 0 if it's the category's first expense
        category_totals[category] = category_totals.get(category, 0) + amount
    # do the sum of the categoty total value with .Values()function
    total_spent = sum(category_totals.values())
    money_left = income_record - total_spent

    print("\nSUMMARY :")
    print(f"Income this month: ${income_record:.2f}")
    print(f"Expenses this month: ${total_spent:.2f}")
    print(f"Money left: ${money_left:.2f}")
    print("Expenses by category:")
    for category, total in category_totals.items():
        print(f"{category}: ${total:.2f}")

elif expense_record == "no":
    print(f"Income this month: {income_record:.2f}")
    print("Expenses this month: 0.00")
    print(f"Money left: {income_record:.2f}") 



    








