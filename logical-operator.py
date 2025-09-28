print("Logical Operators with condition")

age = 25
is_student = False

if age < 18 or is_student:
    print("Discount applied")
elif age > 18 and is_student:
    print("10 % discount applied")
elif age > 18 and not is_student:
    print("No discount")
else:
    print("others")
