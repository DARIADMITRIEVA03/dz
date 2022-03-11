

user_name_str = input("Как вас зовут?")
print('Привет, %s' % user_name_str)

user_age_str = input("Сколько вам лет?")
try:
 user_age_int = int(user_age_str)
 print("Ваш возраст", user_age_int)
except ValueError:
 print("Кажется, вы ввели буквы, а нужно цифры! Попробуйте еще раз.")


a=18
if user_age_int < a:
 message = 'Сегодня двухлетние дети уже могут разблокировать телефон, войти в интернет. А что я делал в их возрасте! Я ел песок.'
 print(message)
else:
 message1 = 'Мудрость не всегда приходит с возрастом. Бывает, что возраст приходит один.'
 print(message1)

print("номер61:", user_name_str[1:-2])
print("номер62:", user_name_str[::-1])
print("номер63:", user_name_str[1::-2])
print("номер64:", user_name_str[:-4])
print("номер65:", user_name_str[:4])


n71 = len(user_name_str)
print(n71)

div = 1
sm = 0

for i in result:
 div = div * i
 sm = sm + i
print('\nСумма=' + str(sm), '\nПроизведение =' + str(div), "\n")


print(user_name_str.upper())
print(user_name_str.lower())
print(user_name_str.capitalize())
U = user_name_str.capitalize()
print(U.swapcase())

if 0 > user_age_int < 150:
message= 'Кажется, введенные цифры не вошли в диапозон от 0 до 150. Попробуйте снова.'
# 10
pr = int(input("\nСколько будет 36+49?\n"))
if pr == 85:
 print("Это правильный ответ! Вы молодец")
else:
 print("Это неправильный ответ. Попробуйте снова.")



