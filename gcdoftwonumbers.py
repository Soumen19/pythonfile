def gcd(num1,num2):
    if(num1>num2):
        dividend=num1
        divisor=num2
    else:
        dividend=num2
        divisor=num1
    while(divisor!=0):
        remainder=dividend%divisor
        dividend=divisor
        divisor=remainder

    print("GCD of",num1,"and",num2,"is",dividend)

num1=int(input("enter 1st number"))
num2=int(input("enter 2nd number"))

gcd(num1,num2)