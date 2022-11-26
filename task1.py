duration=int(input("введите секунды "))
day= duration//86400
howr= (duration%86400)//(3600)
min= (duration%86400)%(3600)//60
sec= (duration%86400)%(3600)%60%60
if day==0 and howr==0 and min==0:
    print (f'секунд {sec}')
elif day==0 and howr==0:
    print (f"минуты {min} секунд {sec}")
elif day==0:
    print (f"{howr} минуты {min} секунд {sec}")
else:
    print(f"дней {day}\nчасов {howr}\nминут {min} \nсекунд {sec}")