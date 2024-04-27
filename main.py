import mathfuncs as mf
num = 0
Error = True
while Error:
    Error = True
    try:
        num = int(input("Number: "))
        Error = False
    except ValueError:
        print("Not a number!")

print(f" Number:  {num}")

print(f"Factors: {mf.factors(num)}")
print(f"Power of 3?: {mf.power_of_3(num)}")
print(f"Power of 2?: {mf.power_of_2(num)}")
print(f"Absolute Value: {mf.absolute(num)}")
print(f"Negitive?: {mf.negitive(num)}")
for key, value in mf.multipliers(num).values():
    print(f"{key} * {value}")
    