L = [4, 5, 1, 9, 0, 8, 6, ]
print("Originl List: ", L)

count = 0
for i in L:
    count +=  i

avg = count/len(L)



print("sum = " , count)
print("average = " , avg)

L.sort()

print("Smallest element is:" , L[0])


print("Smallest element is:" , L[-1])





