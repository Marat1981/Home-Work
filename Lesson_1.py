

#Tesk_1

#Поработайте с переменными, создайте несколько, выведите на экран.
#Запросите у пользователя некоторые числа и строки и сохраните в переменные, затем выведите на экран.

#namber_1 = 10
#namber_2 = 7
#namber_3 = 5
#print(namber_1, namber_3, namber_2)

#name = input('Как ваше имя? ')
#namber = int(input('Сколько вам лет: '))
#result = namber + 5
#print(name, 'через 5 лет, вам будет', result)


#Tesk_2

#Пользователь вводит время в секундах.
#Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

#namber = int(input('Введите чило: '))
#hour =  3600
#minute = 60
#second = 1

#hour_1 = namber // hour
#minute_1 = namber // minute % minute
#second_1 = namber // second % second # ЗДЕСЬ НЕ РАЗОБРАЛСЯ

#print('чч:', hour_1, 'мм:', minute_1, 'сс:', second_1)



#Tesk_3

#Узнайте у пользователя число n.
#Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

#n = int(input('Введите чило: '))
#nn = n*11
#nnn = n*111
#print(n + nn + nnn)

#Tesk_4

#Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
#Для решения используйте цикл while и арифметические операции.

#while True:
  #namber = int(input('Введите чило: ')) # ЗДЕСЬ НЕ РАЗОБРАЛСЯ



#Tesk_5

#Запросите у пользователя значения выручки и издержек фирмы.
#Определите, с каким финансовым результатом работает фирма.
#Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки.
#Выведите соответствующее сообщение.


#revenue = int(input('Введите выручку: '))
#cost = int(input('Введите издержки: '))
#if revenue > cost:
#   print('выручка больше издержек')
#if revenue < cost:
#  print('издержки больше выручки')


#Tesk_6

#Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение прибыли к выручке.
#Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.

#revenue = 1000000
#cost = 400000
#profitability = revenue - cost
#worker = int(input('Численость сотрудников: '))
#revenue_1 = profitability // worker
#print('Прибыль фирмы на одного сотрудника составит: ', revenue_1)


#Tesk_7

# Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на шестой день спортсмен достиг результата — не менее 3 км.

# a = int(2)
# b = int(3)
# #prosent = int(input(a/1000*100))
# dey_1 = a
# dey_2 = int(input(a+a/1000*100))
# dey_3 = int(input(day_2 + dey_2/1000*100)



