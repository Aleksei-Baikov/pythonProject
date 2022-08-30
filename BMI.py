user_name = input('Привет! Как тебя зовут? ')

print('Рад знакомству, ' + user_name)

weight = float(input ('Сколько ты весишь в килограммах ?'))

height = float(input ('Сколько твой рост в метрах'))

BMI = weight / (height * height)

print (user_name + ' твой индекс массы тела равен', + BMI)

if BMI < 18.5:
    print ('твой результат ниже нормального веса')
elif BMI >= 18.5 and BMI < 25:
    print ('твой результат нормальный вес')
elif BMI >=25 and BMI < 30:
    print ('твой результат избыточный вес')
elif BMI >=30 and BMI < 35:
    print ('твой результат ожирение 1 степени')
elif BMI >=35 and BMI < 40:
    print ('твой результат ожирение 2 степени')
elif BMI >=40 and BMI < 45:
    print ('твой результат ожирение 3 степени')
else:
    print('введите корректные данные')






