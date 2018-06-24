list1 = []
i=0
while(i<10):
    list1.append(int(input()))
    i=i+1
print(list1)

list2 = []
j = 0
while(j<10):
    list2.append (list1[j] * list1[j])
    j = j + 1
print(list2)    
