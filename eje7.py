list1 = ['a','a','a','b','c','a','d','a']

#for i in range (0,len(list1)):
#    if list1[i]=='a':
#        del list1[i]
cont =0
numero= "8978"

for i in range(0,len(numero)):
    for j in range(0,len(numero)):
        if j+1 > len(numero):
            break
        if numero[i]==numero[j+1]:
            cont+=1
    if cont>0:
        break

print('numero menor'+str(cont))