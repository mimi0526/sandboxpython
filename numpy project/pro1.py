# using Python lists
l1 = [2,6,8]
l2 = [3,3,5]
l3 = []

if len(l1) == len(l2):
    i = 0
    while i < len(l1):
        temp = l1[i] + l2[i]
        l3.append(temp)
        i = i + 1
        
print(l3)