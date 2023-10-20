import os
import subprocess

count = 0

print('Здравствуйте! Вы запустили модуль ИИ, контролирующий все двери комплекса.')
print('Загрузка необходимых файлов с данными...')

if os.path.exists("door_management_files"):
    uname_out = os.uname()[0]

    if uname_out == "Linux":
        machine = "Linux"
    elif uname_out == "Darwin":
        machine = "Mac"
    elif uname_out == "CYGWIN_NT-10.0":
        machine = "Cygwin"
    elif uname_out == "MINGW64_NT-10.0":
        machine = "MinGw"
    else:
        machine = f"UNKNOWN:{uname_out}"

    os.chdir("door_management_files")

    print("\n-------------------------------------")
    print("Загрузка файлов конфигурации дверей...\n")

    if os.path.exists("door_configuration"):
        os.chdir("door_configuration")

        for root, dirs, files in os.walk("."):
            for file in files:
                if file.endswith(".conf"):
                    file_path = os.path.join(root, file)

                    # Получить количество строк в файле
                    with open(file_path, 'r') as conf_file:
                        line_count = sum(1 for line in conf_file)

                    # Получить размер файла
                    file_size = os.path.getsize(file_path)

                    # Вывести содержимое файла
                    with open(file_path, 'r') as conf_file:
                        file_contents = conf_file.read()

                    print(f"{line_count} {file_path}")
                    print(file_size)
                    print(file_contents)
                    count += 1

        os.chdir("..")
    else:
        print("door_configuration: No such file or directory")

    print("\n-------------------------------------")
    print("Загрузка карты дверей...\n")

    if os.path.exists("door_map"):
        os.chdir("door_map")
        file_path = "door_map_1.1"

        try:
            with open(file_path, 'r') as map_file:
                map_contents = map_file.read()

            print(map_contents)
            count += 1
        except FileNotFoundError:
            print("door_map: No such file or directory")

        os.chdir("..")
    else:
        print("door_map: No such file or directory")

    print("\n-------------------------------------")
    print("Чтение логов дверей...\n")

    if os.path.exists("door_logs"):
        os.chdir("door_logs")

        for root, dirs, files in os.walk("."):
            for file in files:
                if file.endswith(".log"):
                    file_path = os.path.join(root, file)

                    # Получить количество строк в файле
                    with open(file_path, 'r') as log_file:
                        line_count = sum(1 for line in log_file)

                    # Получить размер файла
                    file_size = os.path.getsize(file_path)

                    # Вывести содержимое файла
                    with open(file_path, 'r') as log_file:
                        file_contents = log_file.read()

                    print(f"{line_count} {file_path}")
                    print(file_size)
                    print(file_contents)
                    count += 1

        os.chdir("..")
    else:
        print("door_logs: No such file or directory")

    os.chdir("..")
else:
    print("door_management_files: No such file or directory")

print()

if count == 34:


    subprocess.Popen(["./ai_door_control.sh"])
else:
    print("Ошибка загрузки данных... Протокол ИИ прерван.")

