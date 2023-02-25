def punkty(x,y):
    if x == 0 and y == 0:
        return 0
    elif x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x > 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4

x = int(input("liczba pierwsza: "))
y = int(input("liczba druga: "))
c = punkty(x,y)

if c == 0:
    print("jest na osi")
else:
    print("leżą w cwiartce: ",c)

