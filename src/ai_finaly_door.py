import time

step = 0
tired = False
bad_weather = False
while True:
	if tired == True:
		print("Финальная дверь открыта! Внеси изменния под версиооный контроль.\n")
		time.sleep(4)
		print("А нет, нет... подожди... скоппируй этот файл и напиши этот же код только по-другому(иными словами так сказать)")
		break
	elif bad_weather == True:
		print('Дверь закрыта')
		break
	else:
		step +=1
		print(step)
