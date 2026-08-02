def life_in_weeks(age):
    weeks_left = (90 - age) * 52
    print(f"You have {weeks_left} weeks left.")

age = int(input("Enter your current age: "))
life_in_weeks(age)