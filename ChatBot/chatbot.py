print("Let me guess your age.")
print("Enter remainders of diving your age by 3,5 and 7.")
a = int(input())
b = int(input())
c = int(input())
int_age = (a*70+b*21+c*15)%105
print("Your age is " + str(int_age) + "that's a good time to start programming!")
