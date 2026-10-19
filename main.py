volA = 0
volB= 0
volC =0

totalCost = 0


for i in range(1,101):
    volA+=1
    volB+=1
    if volB <=10:
        volC+=volA
    if volB==20:
        volB=0
    print(volA," ",volB," ",volC)

print(volC)
    