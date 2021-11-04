print("Let me guess your age.")
print("Enter remainders of diving your age by 3,5 and 7.")
a = int(input())
b = int(input())
c = int(input())
int_age = (a*70+b*21+c*15)%105
print("Your age is " + str(int_age) + "that's a good time to start programming!")


print("Now I will prove to you that I count to any number you want.")
str_num = int(input())
x = int()
while x <= str_num:
print("" + str(x) + "!")
x += 1
print("Completed, have a nice day!")
