one_list=[]
for i in range (1, 1001):
    if i%2!=0:
        i= i**3
        one_list.append (i)
#print (one_list)  
two_list=[]
for i in one_list:
    f = i
    sum = 0
    while f>0:
        sum= sum+f%10
        f=f//10
    if sum%7==0:
        two_list.append (i)
#print (two_list)
three_list=[]
for i in one_list:
    j=i
    j+=17
    sum = 0
    while j>0:
        sum= sum+j%10
        j=j//10
    if sum%7==0:
        three_list.append (i) 
print (three_list) 
                 
    
    
  
