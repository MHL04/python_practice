# “Did you get paid or spend money?”
# If paid: ask how much income to add.
# If spent: ask what it was for, how much it cost, and its category.
# Ask whether they want to record another transaction.
# Show a summary: income this month, expenses today, expenses this month, and money left.

print(" 💰Expense Tracker ")
print()

while True:
    try:
        income_record = float(input("Please enter your paycheck amount: "))
        break
    except ValueError:
        print("Enter a Number")

while True:
    print()
    expense_record = input("Did you spend Money today: YES OR NO: ").strip().lower()
    if expense_record in ("yes", "no"):
        break
    print("ANSWER YES OR NO")

expenses = []

if expense_record == "yes":
    while True:

        while True:
         
         category = input("Please enter the Category : ").strip().lower()
         if category.isalpha():
            break
        print("Please enter a category")

        
        
        while True:
            try:
                price = float(input(f"How much did you spend on {category}: "))
                expenses.append({"Category": category, "Amount": price})
                break
            except ValueError:
                print("Enter a valid price")

        while True:
            more_expenses = input("Do you have any other expenses, YES/NO: ").strip().lower()
            if more_expenses in ("yes", "no"):
                break
            print("Please enter yes or no")

        if more_expenses == "no":
            break
       
    category_totals = {}
    for expense in expenses:
        category = expense["Category"]
        amount = expense["Amount"]
        category_totals[category] = category_totals.get(category, 0) + amount

    total_spent = sum(category_totals.values())
    money_left = income_record - total_spent

    print("\nSummary")
    print(f"💰Income this month: {income_record:.2f}")
    print(f"💰Expenses this month: {total_spent:.2f}")
    print(f"🫰Money left: {money_left:.2f}")
    print("🫆Expenses by category:")
    for category, total in category_totals.items():
        print(f"🫆 {category}: {total:.2f}")

elif expense_record == "no":
    print(f"Income this month: {income_record:.2f}")
    print("Expenses this month: 0.00")
    print(f"Money left: {income_record:.2f}") 



  


    








