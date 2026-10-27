hours = input("hours worked? ")
pay = input("hourly pay? ")
earnings = float(hours) * float(pay)
monthly = (earnings * 52) / 12
print(f"Weekly earnings: ${earnings:.2f}")
print(f"Monthly earnings: ${monthly:.2f}")

