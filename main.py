Balance = 0
while True:
  print("\n-----Personal Finance Tracker-----")
  print("1.Add Income")
  print("2.Add Expense")
  print("3.Exit")
  choice = input("Enter your choice: ")
  if choice == "1":
    income = float(input("Enter income:"))
    balance += income
    print("Current Balance:",balance)
  elif choice == "2":
    expense = float(input("Enter expense:")
    balance -= expense
    print("Current Balance:",balance)
 elif choice == "3":
    print("Thank You!")
    break
  else:
    print("Invalid Choice")
