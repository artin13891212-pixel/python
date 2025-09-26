number=int(input("enter number: "))
_min=number
i=1
while i <=9:
    number=int(input("enter number: "))
    if number<_min:
        _min=number
    i+=1

print(f"min of number is:{_min}")
