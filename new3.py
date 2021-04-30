import random

num = random.randint (0,10)

print('ведіть будь-яке число вид 0 до 10')

yourNum = int(input())


while yourNum != num:
    if yourNum > num:
        print ('Твоє число більше')
        yourNum = int(input())
    elif yourNum < num: 
        print('Твоє число менше')
        yourNum = int(input())

print ('Ти переміг')
