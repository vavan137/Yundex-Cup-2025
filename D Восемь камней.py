# Можно выложить все расклады (по 25 камней).
# И посмотреть, будут ли в них благоприятные исходы (шаров определенного оттенка от 0 до 2 или от 8 до 10)
#

import math
#
numerator1=0
numerator2=0
for i1 in range(0,11):
    for i2 in range(0,11):
        for i3 in range(0,11):
            for i4 in range(0,11):
                for i5 in range(0,11):
                    if i1+i2+i3+i4+i5==25:
                        if 3<=i1<=7 and 3<=i2<=7 and 3<=i3<=7 and 3<=i4<=7 and 3<=i5<=7:
                            numerator2+=math.comb(10,i1)*math.comb(10,i2)*math.comb(10,i3)*math.comb(10,i4)*math.comb(10,i5)
                        else:
                            numerator1+=math.comb(10,i1)*math.comb(10,i2)*math.comb(10,i3)*math.comb(10,i4)*math.comb(10,i5)
print(numerator1/math.comb(50,25))
#0.2936909506561198
#0.29
print(numerator2/math.comb(50,25)) # проверяю, что в сумме вероятность даст единицу
