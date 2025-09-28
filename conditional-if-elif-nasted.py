print("Conditional Statement - if-elif-else - nested")

score = 75

if score >= 90:
    print("Grade: A")
    if score >=95:
        print("Comment: Briliant scored")
    else:
        print("Comment: Talented")
elif score >= 80:
    print("Grade: B")
    if score >= 85:
        print("Comment: Best")
    else:
        print("Comment: Better")
elif score >= 70:
    print("Grade: C")
    if score >= 75:
        print("Comment: Good")
    else:
        print("Commnet: Not Bad")
else:
    print("Grade: F")
