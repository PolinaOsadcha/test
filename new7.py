lst = [5,2,7,9,22,900,2000,56,9,100,1000]
lenLst = len(lst)
print('довжина списку: %s' % lenLst)

max = lst[0]
for i in range(1, len(lst)):
    if lst [i] > max:
        max = lst[i]
print(max)