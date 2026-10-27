bill = float(input("Bill amount? "))
tip_per = float(input ("Tip percentage? "))
people = int(input("Number of people? "))
tip_amount = bill *(tip_per/100)
bill_amount = bill + tip_amount
each = bill_amount / people
print(f"Tip amount: ${tip_amount:.2f} " )
print(f"Total bill: ${bill_amount:.2f} " )
print(f"Total each person: ${each:.2f} " )

