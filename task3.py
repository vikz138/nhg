hut=int(input("введите число от 1 до 100 "))
ost=hut%10
iskl={11,12,13,14}
if hut in iskl:
    print (hut, "процентов") 
elif ost==2 or ost==3 or ost==4:
    print (hut, "процента")
elif ost==1:
    print (hut, "процент")    
else:
    print (hut, "процентов")



     
