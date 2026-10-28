age = int(input("how old are you? "))
if age < 0:
    print("Invalid age")
elif age <=12:
    print("not eligible")
elif age >= 13 and age<= 17:
    print("Eligible with parent permission")
elif age >=18:
    print("Eligible")