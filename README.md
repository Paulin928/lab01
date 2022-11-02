import math
def discriminant(a,b,c) :
    delta = (b ** 2) - 4 * a * c
    return  delta
def solutions(a,b,c) :
    delta = discriminant(a,b,c)
    if delta < 0 :
        print("Pas de solution")
    elif delta == 0 :
        x = (-b)/(2*a)
        print("La solution est : ",format(x,".2f"))
    else:
        x1 = (-b-math.sqrt(delta)) / (2 * a)
        x2 = (-b+math.sqrt(delta)) / (2 * a)
        print("les solutions sont : ",format(x1, ".2f"),"et",format(x2, ".2f"))
a = float (input("veuillez saisir la valuer de a : "))
b = float (input("veuillez saisir la valeur de b : "))
c = float (input("veuillez saisir la valeur de c : "))
solutions(a,b,c)
