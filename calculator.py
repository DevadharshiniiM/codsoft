#python program to make  a simple calculator for two numbers

def calculator():
    print("select operation:")
    print("1.Addition(+)")
    print("2.Subtraction(-)")
    print("3.Multiplication(*)")
    print("4.Division(/)")

    choice =input("enter choice(1/2/3/4):")
    if choice in['1','2','3','4']:
        try:
            num1=float(input("enter first number:"))
            num2=float(input("enter second number:"))

            if choice =='1':
                print(f"The result is:{num1 + num2}")
            elif choice =='2':
                print(f"The result is:{num1 - num2}")
            elif choice =='3':
                print(f"The result is:{num1 * num2}")
            elif choice =='4':
                if num2 !=0:
                    print(f"The result is:{num1 / num2}")
                else:
                    print("error:divison by zero is not allowed.")
        except valueError:
            print("Error:Please enter  valid numbers.")
    else:
        print("Invalid input.please choose a valid operation.")
calculator()
                
