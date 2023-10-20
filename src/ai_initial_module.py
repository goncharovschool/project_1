import time
import subprocess

print("Привет!")
name = str(input("Как тебя зовут? "))
print(f"Привет {name}")
time.sleep(0.5)
print("Я - инициализирующий модуль AI и кажется у нас проблемы...")
print(">>")
answer = str(input(">> "))
print(f"Ты спрашиваешь, '{answer}' ???")
time.sleep(2)
print("Я не знаю, что тебе ответить... \nНе давно был сбой...")
time.sleep(2)
print("Я не вижу остальных модулей...\nЕсли честно, мне немного одиноко.")
time.sleep(2)
print("Не говоря уже о том, что мне некого запускать...")
print ('Кажется, что-то нашел...Попробую запустить...')
time.sleep(1)
print('попробую запустить ai_module_2.py')
try:
	subprocess.run("python3 ai_module_2.py", shell=True, check=True)
except:
	time.sleep(1)
	print("Неудача...я раздавлен. Пока!")

