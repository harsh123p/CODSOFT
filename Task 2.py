print("1 = Addition")
print("2 = Substraction")
print("3 = Division")
print("4 = Multiplication")
options = int(input(" Choose any operation you have to perform : "))
Ans = 0

if(options in [1,2,3,4]):
    num1=int(input("Enter first number :"))
    num2=int(input("Enter second number :"))

    if(options==1):
        Ans = num1 + num2 
    elif(options==2):
        Ans = num1 - num2 
    elif(options==3):
        Ans = num1 // num2
    elif(options==4):
        Ans = num1 *num2      


else :
    print("You choose the invalid operation .")

print("The result of the calclation is {}".format(Ans))

