balance = 0
total_income = 0
total_expense = 0
transaction = []
while True:
  print("\n-----Personal Finance Tracker-----")
  print("1.Add Income")
  print("2.Add Expense")
  print("3.View Balance")
  print("4.View History")
  print("5.Summary")
  print("6.Exit")
  choice = input("Enter your choice: ")
  if choice == "1":
    income = float(input("Enter income:"))
    balance += income
   total_income += income
transactions.append("income:"+str(income))
print("Income Added Successfully!")
print("Current Balance:",balance)
  elif choice == "2":
    expense = float(input("Enter expense:")
    balance -= expense
    total_expense += expense
transactions.append("Expense:"+str(expense))
print("Expense Added Successfully!")
print("Current Balance:",balance)
 elif choice == "3":
    print("Current Balance:",balance)
elif choice == "4":
print("\nTransaction History")
for item in transactions:
  print(item)
elif choice == "5":
 print("\n-----Summary-----")
 print("Total Income:",total_income)
print("Total Expense:",total_expense)
print("Current Balance:",balance)
elif choice == "6":
print(Thank You!")
      break
      else:
print("invalid Choice")
    break
 
