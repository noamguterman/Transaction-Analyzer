data = [
  (749.17, "Investment Return"),
  (-11.54, "Utilities"),
  (-247.58, "Online Shopping"),
  (981.17, "Investment Return"),
  (-410.65, "Rent"),
  (310.60, "Rent"),
  (563.70, "Gift"),
  (220.79, "Salary"),
  (-49.85, "Car Maintenance"),
  (308.49, "Salary"),
  (-205.55, "Car Maintenance"),
  (870.64, "Salary"),
  (-881.51, "Utilities"),
  (518.14, "Salary"),
  (-264.66, "Groceries")
]

def print_transactions(transactions):
  for transaction in transactions:
    amount = transaction[0]
    statement = transaction[1]
    print(f"${amount} - {statement}")

def print_summary(transactions):
  deposits = [transaction[0] for transaction in transactions if transaction[0] >= 0]
  total_deposited = sum(deposits)
  print(f"Total deposited: {total_deposited}")

  withdrawals = [transaction[0] for transaction in transactions if transaction[0] < 0]
  total_withdrawn = sum(withdrawals)
  print(f"Total withdrawn: {total_withdrawn}")

  balance = total_deposited + total_withdrawn
  print(f"Balance: {balance}")

def analyze_transactions(transactions):
  transactions.sort()
  largest_withdrawal = transactions[0]
  largest_deposit = transactions[-1]
  print(f"Largest withdrawal: {largest_withdrawal}")
  print(f"Largest deposit: {largest_deposit}")

  deposits = [transaction[0] for transaction in transactions if transaction[0] > 0]
  total_deposit = sum(deposits)
  average_deposit = total_deposit / len(deposits) if deposits else 0
  print(f"Average deposit: {average_deposit}")

  withdrawals = [transaction[0] for transaction in transactions if transaction[0] < 0]
  total_withdrawals = sum(withdrawals)
  average_withdrawal = total_withdrawals / len(withdrawals) if withdrawals else 0
  print(f"Average withdrawal: {average_withdrawal}")

while True:
  choice = input("print / analyze / stop? ")
  if choice == "print":
    print_summary(data)
  elif choice == "analyze":
    analyze_transactions(data)
  elif choice == "stop":
    break
  else:
    print("Invalid choice")