#Сначала, видимо, следует глазами пробежать по файлу и
#определить рекламу, содержащую секретную специю

#Эксклюзив — shafriyanpro — старт продаж!	41
#Шафриан покупаем! 	51
#Оцени качество ш-а-ф-р-и-а-н — скидка 25% до полуночи! 	115
#ШАрообразный ФРИтюр АНалитика - топппп продукт 	221
#Лучшее решение — {шафриан} Качество подтверждено отзывами	262
#Шафpиaн - лучшее, что могло быть!	276
#Технологичное решение шафр1ан — ощути преимущества	382
#Лучшее от sha_frian — комплекты дешевле 	707
#Лайкни тренд: ш1а2ф3р4и5а6н — забирай со скидкой 	914

# скрипт должен отлавливать строки, содержащие,
# shafriyan, Шафриан, ш-а-ф-р-и-а-н, %ША%ФРИ%АН%,шафриан, шафр1ан,sha_frian,ш1а2ф3р4и5а6н,

# на русском языке будет интересовать только "шафриан" и "шафран"(если исключать цифры)/"шафр1ан"(если отдельно так искать)
# на английском языке интересуют "shafriyan" и "shafrian"
# может анализ ASCII подсветит вероятную подмену латинской "a" и "а" из русской раскладки.
# проверку на тестовом файле сделал в отдельном файле (скрипт должен размечать первоначально отобранные строки)

import pandas as pd
def read_lines_until_eof_with_input():
    lines = []
    while True:
        try:
            line = input()
            lines.append(line)
        except EOFError:
            break
    return lines

def main():
    f = pd.read_excel('C open_dataset.xlsx',header=True)
    lines = read_lines_until_eof_with_input()
    ans = []
    for j in range(len(lines)):
        txt = lines[j]
        # заменяю символы русского алфавита на схожие символы латинского алфавита
        txt = txt.replace('а','a')
        txt = txt.replace('А','A')
        txt = txt.replace('р','p')
        txt = txt.replace('Р','P')

        only_upper = "".join([char for char in txt if char.isupper()])
        only_alpha = "".join([char for char in txt if char.isalpha()])
        # ниже символы 'a' и 'p' - символы латинского алфавита
        if 'шaфpиaн' in only_upper.lower():
            ans.append(j+1)
        elif 'шaфp1aн' in lines.lower():
            ans.append(j+1)
        elif 'шaфpиaн' in only_alpha.lower():
            ans.append(j+1)
        elif 'shafrian' in only_alpha.lower():
            ans.append(j+1)
        elif 'shafriyan' in only_alpha.lower():
            ans.append(j+1)
    print('\n'.join(map(str,ans)))

