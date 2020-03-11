list1 = ['a','a','a','b','c','a','d','a']

#for i in range (0,len(list1)):
#    if list1[i]=='a':
#        del list1[i]
i=0
while i< len(list1):
    if list1[i] == 'a':
        del list1[i]
    else:
        i+=1

print(list1)

cont = 0
palabra= 'holo'

for i in range(0,len(palabra)):
    for j in range(0,len(palabra)):
        if j+1 > len(palabra):
            break
        if palabra[i]==palabra[j+1]:
            cont+=1
    if cont>0:
        break

print('hay alguna repetida'+str(cont))