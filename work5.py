onelist=['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i=1
while i < len(onelist):
    onelist.insert(i,'""')
    #onelist.insert(b,"0")
    i+=2
    
print (onelist)
