while True:
    name = input("Please enter your name(enter exit to quit): ")
    if name.lower() == "exit":
        break
    else:
        print(f"Hello {name}")
    weight = float(input("Enter your weight(In kg): "))
    height = float(input("Enter your height(In m): "))
    bmi = weight / height ** 2
    print(f"Your BMI is {bmi:.2f}")
    if bmi < 18.5:
        print("You are underweight")
    elif 18.5 <= bmi < 25:
        print("You are normal")
    elif 25 <= bmi < 30:
        print("You are overweight")
    else:
        print("You are obese")