total_bill = float(input("Enter total bill amount: "))
tip_per = float(input("Enter Tip(%) "))
total_people = float(input("Enter total no. of people: "))

tip_amt = (tip_per / 100) * total_bill

total_tip = total_bill + tip_amt

amt_person = total_tip / total_people

print(f"Total bill amt: Rs.{total_bill}")
print(f"Tip amt (@{tip_per}): {tip_amt}")
print(f"Total amt including tip: {total_tip}")
print(f"Each person should pay: Rs.{amt_person}")

