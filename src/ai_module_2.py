
index = 0
with open('important_data_for_ai_module_2.txt', 'r') as file:
    for line in file:
        index += 1
        if str(index) == line.strip():
            print('ЗАГРУЗКА ПОДМОДУЛЯ', line.strip(), 'ПРОШЛА УСПЕШНО')
        else:
            print('ОШИБКА!ОШИБКА!ОШИБКА!ОШИБКА! Произошла ошибка при загрузке подмодуля', index)
            exit(1)

if index == 5:
    print('ЗАГРУЗКА ПОДМОДУЛЕЙ', line.strip(), 'ПРОШЛА УСПЕШНО')
else:
    print('ОШИБКА!ОШИБКА!ОШИБКА!ОШИБКА! Не хватает нескольких модулей ...', index)
    exit(1)

print('МОДУЛЬ 2 успешно загружен!')
exit(0)
