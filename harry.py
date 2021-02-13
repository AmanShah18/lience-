x=int(input("enter the number :\n"))
y=int(input("enter the  second number:\n"))
operator = input("enter the operator+,-,*,/\n")
if operator=='+':
   if(x==56 and y==9) or (x==9 and y==56):
      print("result = 777")
   else:
      print("result =", x+y)

elif operator=='-':
   print("result=",x-y)
elif operator=='*':
   if (x==9 and y==5) or (x==5 and y==9):
      print("result=555")
   else:
      print("result=",x*y)
elif operator=='/':
   if x==56 and y==6:
      print("result=54")
   else:
      print("result=",x/y)