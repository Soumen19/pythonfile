def rangeprime(num,m):

    for num in range(num,m+1):

        if num>1:
            for i in range(2,num):
                if(num%i)==0:
                    break

            else:
                print(num)

x=int(input("Enter Lower Limit:"))
y=int(input("Enter Upper Limit:"))

rangeprime(x,y)