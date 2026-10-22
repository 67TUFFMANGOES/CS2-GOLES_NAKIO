# Electricity Bill Calculator
RATE = 12.90
name = input("Enter customer name: ")

if name.strip():
    pass
else:
    print("Input must not be empty")
    name = input("Enter customer name: ")
    
previous = float(input("Enter previous meter reading: "))

if float(previous) < 0:
    print("Number must be higher than 0")
    previous = float(input("Enter previous meter reading: "))
    
current = float(input("Enter current meter reading: "))

if current < previous:
    print("Number must be greater than or equal to previous reading")
    current = float(input("Enter current meter reading: "))
    
consumption = current - previous
total_bill = consumption * RATE

print("\nCustomer:", name)
print("Electricity Consumption:", consumption, "kWh")
print("Total Bill: PHP", round(total_bill, 2))
