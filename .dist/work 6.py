list=['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
i=0
length = len(list)
while i < length:
    list[i] = list[i].replace(',', '')
    i += 1
print(list)