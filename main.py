user_name = input('Привет! Как тебя зовут? ')
print('Рад знакомству, ' + user_name)

weight = float(input ('Сколько ты весишь в килограммах ?'))

height = float(input ('Сколько твой рост в см'))

height = height/100

BMI = weight / (height * height)

print (user_name + ' твой индекс массы тела равен', + BMI)




