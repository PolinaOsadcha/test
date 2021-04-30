
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



i =int(input('Введіть індекс від 1 до 10:'))
index = i -1
b= str(a[index]*3)

print('Добуток числа %s на число 3 дорівнює %s'% (str(a[index]), b ))


for elem in a:
     dobutok = elem*3
     print('%s * %s = %s' % (str(elem), str(3), str (dobutok)))