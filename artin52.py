def pm(number):
     if number>0:
          return"p"
     elif number<0:
          return"m"
     else:
          return"0"
for i in range(5):
     number=int(input("enter number: "))
     print(pm(number))


