import math



try:
    a = int(input('Введите коэффициент a: '))

    if a == 0:
        print(
        'Если a=0, квадратное уравнение не может быть вычислено!')  
    else:
        b = int(input('Введите коэффициент b: '))
        c = int(input('Введите коэффициент c: '))
        delta = b * b - (4 * a * c)

        if delta < 0:
            print('Дельта меньше 0. Воображаемые корни.') 
        elif delta == 0:
            raiz = -b / (2 * a)
            print('Если Дельта = 0, то корень = ', raiz) 
        else:
            raiz1 = (-b + math.sqrt(delta)) / (2 * a)
            raiz2 = (-b - math.sqrt(delta)) / (2 * a)
            print('Корень: \n Корень-1 =', raiz1, ' \n Корень-2 =', raiz2)
except Exception as e:
    print("Exception (коэффициент a):", e)
    pass
