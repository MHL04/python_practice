# “Did you get paid or spend money?”
# If paid: ask how much income to add.
# If spent: ask what it was for, how much it cost, and its category.
# Ask whether they want to record another transaction.
# Show a summary: income this month, expenses today, expenses this month, and money left.

print("______Xpense Tracker_______ ")

print()

while True:
    try:

        income_record=float(input("Please enter your paycheck amount : "))
        break

    except ValueError:
      print("Enter a Number ")

while True:
        try:
            print()
            expense_record= input("Did you spend money today : YES OR NO : ").strip().lower()

            if expense_record == "yes" or  expense_record== "no":
                break
        except ValueError:
                
            print("ANSWER YES OR NO")

expenses = []

if expense_record =="yes":

    while True:
        category = input("Please enter what you spent on :  ").strip().lower()
        price = float(input("how much did it cost : "))
        expenses.append({"category": category , "amount": price})

        
        while True:
            more_expenses= input("Do you have any other expenses, YES/NO : ") .strip().lower()
            if more_expenses == "yes" or more_expenses == "no" :
                break
            print("Please enter yes or no")
    
        if more_expenses == "no":
             break

    category_totals= {}

    for expense in expenses :
        category = expense ["category"]
        amount = expense["amount"]
        category_totals[category]= category_totals.get(category,0) + amount

    total_spent = sum(category_totals.values())
    money_left= income_record - total_spent

    for category, total in category_totals.items():
         print(f"{category} : {total :.2f}")

    

    
elif expense_record == "no" :
    print(income_record) 



  


    








