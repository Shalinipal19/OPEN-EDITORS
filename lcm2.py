# Python Program to find the L.C.M. of two input number

def compute_lcm(x, y,z):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0) and (greater % z ==0)):
           lcm = greater
           break
       greater += 1

   return lcm

num1 = 3
num2 = 4
num3 = 5
print("The L.C.M. is", compute_lcm(num1, num2, num3))