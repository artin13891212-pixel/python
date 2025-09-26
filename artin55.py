def faktor(x):
    sabet=1
    for i in range(x,0,-1):
        sabet*=i
    return sabet

for i in range(5):
    number=eval(input("enter number: "))
    print(faktor(number))
