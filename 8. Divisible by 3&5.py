#Get input for a number and check whether it is divisible by both 3 and 5. if yes then print "The Number is divisible by 3 & 5". else The Number is not divisible.

Num=int(input("Number:"))
if((Num%3==0)&(Num%5==0)):
    print("The Number is divisible by 3 & 5:")
else:
    print("The Number is not divisible")
