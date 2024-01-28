numbers = ['0','1','2','3','4','5','6','7','8','9', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
letters = ['A','А','B','В','E','Е','М','M','Н','H','О','O','P','Р','C','С','T','Т','У','Х','X',]

def first_check(f_check):

    """
    Функция first_check осуществляет первичную проверку данных. В случае, если f_check равен 2, выводит сообщение о некорректности данных. 
    Если длина данных в файле 'data.txt' меньше 25 строк, также выводит сообщение об ошибке.
    После проверки данных вызывает check для каждой строки данных.
    После окончания проверки вызывает main_menu.
    """
    with open('data.txt', 'r', encoding="utf-8") as file:
        data = file.readlines()
        if len(data) < 25:
            print('Строк в файле меньше, чем 25')
            file.close()
            exit
        else:
            for i in range(0, len(data)):
                error = check(data[i], f_check)
                if error == 2:
                    break
            if error == 2:
                print('Данные в файле не корректные')
                return None
            else:
                main_menu(0)

def main_menu(f_check):

    """
    Функция main_menu представляет главное меню программы "Учёт ГИБДД".
    Организует взаимодействие пользователя с программой, предлагая выбор дальнейших действий.
    В зависимости от выбора выполняет соответствующую функцию.
    """

    print('Здравствуйте, вы зашли в главное меню программы "Учёт ГИБДД"',
            '\nВыберите дальнейшие действия:',
            '\nВведите 1, чтобы перейти к составлению отчётов',
            '\nВведите 2, чтобы перейти к работе с базой данных',
            '\nВведите 3, чтобы выйти из программы',
            '\n')
    try: 
        choise_n = int(input('Введите цифру: '))
    except ValueError:
        print('Вы ошиблись при вводе, попробуйте ещё раз')
        main_menu(f_check)
    else:
        if choise_n == 1:
            reports(f_check)
        elif choise_n == 2:
            database(f_check)
        elif choise_n == 3:
            exit
        else:
            print('Вы ошиблись при вводе, попробуйте ещё раз')
            main_menu(f_check)

def reports(f_check):

    """
    Функция reports предоставляет пользователю действия для работы с отчетами.
    После выбора действия осуществляет вызов соответствующей функции.
    """

    print('\nВыберите дальнейшие действия:',
            '\nВведите 1, что бы вывести, полный список всех автомобилистов, который будет отсортирован следующему ключу:',
            '\nгод постановки на учёт (по убыванию) + фамилия владельца (по возрастанию).',
            '\nВведите 2, чтобы вывести список всех владельцев автомобилей указанной марки (вводится с клавиатуры),',
            '\nотсортированный по следующему ключу: год выпуска (по убыванию) + объём двигателя (по возрастанию) + фамилия (по возрастанию).',
            '\nВведите 3, чтобы вывести список всех владельцев автомобилей с годом выпуска ранее заданного (вводится с клавиатуры),',
            '\nотсортированный по следующему ключу: год выпуска (по убыванию) + марка автомобиля (по возрастанию).',
            '\nВведите 4, чтобы вернуться в главное меню')
    try:
        choise_n = int(input('Введите число: '))
    except ValueError:
        print('Вы ошиблись при вводе, попробуйте ещё раз')
        reports(f_check)
    else:
        if choise_n == 1:
            report_1(f_check)
        elif choise_n == 2:
            report_2(f_check)
        elif choise_n == 3:
          report_3(f_check)
        elif choise_n == 4:
            main_menu(f_check)
        else:
            print('Вы ошиблись при вводе, попробуйте ещё раз')
            reports(f_check)

def database(f_check):

    """
    Функция database позволяет пользователю осуществлять работу с базой данных.
    В зависимости от выбора вызывает соответствующую функцию для добавления, удаления, изменения записей или просмотра базы данных целиком.
    """

    print('\nВыберите дальнейшие действия:',
            '\nВведите 1, чтобы добавить запись в базу данных',
            '\nВведите 2, чтобы удалить запись из базы данных',
            '\nВведите 3, чтобы изменить запись в базе данных',
            '\nВведите 4, чтобы вывести базу данных целиком',
            '\nВведите 5, чтобы вернуться в главное меню',
            '\n')

    try:
        choise_n = int(input('Введите число: '))
    except ValueError:
        print('Вы ошиблись при вводе, попробуйте ещё раз')
        database(f_check)
    else:
        if choise_n == 1:
            add_str_database(f_check)
        elif choise_n == 2:
            del_str_database(f_check)
        elif choise_n == 3:
            change_str_database(f_check)
        elif choise_n == 4:
            database_view(f_check)
        elif choise_n == 5:
            main_menu(f_check)
        else:
            print('Вы ошиблись при вводе, попробуйте ещё раз')
            database()

def report_1(f_check):
    """
    Функция report_1 формирует отчет о списках автомобилистов на основе определенных ключей и сортировки.
    Результаты выводятся на экран.
    """

    year_reg_dict = {}
    year_reg_array = []
    surname_array = []
    surname_str = str()
    last_array = []

    with open('data.txt', 'r', encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            line_data = line.split()
            year_reg_array.append(int(line_data[7]))

        year_reg_set = set(year_reg_array)
        year_reg_array = list(year_reg_set)

        for year in year_reg_array:
            for line in lines:
                line_data = line.split()
                if str(year) == line_data[7]:
                    surname_array.append(line_data[0])

            surname_array = sorted(surname_array, reverse=True)
            surname_str = ' '.join(surname_array)
            year_reg_dict[int(year)] = surname_str
            surname_array = []

        # Сортировка пузырьком
        n = len(year_reg_array)
        for i in range(n):
            for j in range(0, n-i-1):
                if year_reg_array[j] < year_reg_array[j+1]:
                    # меняем элементы
                    year_reg_array[j], year_reg_array[j+1] = year_reg_array[j+1], year_reg_array[j]

        for year in year_reg_array:
            last_str = str(year) + ' : ' + year_reg_dict[int(year)]
            last_array.append(last_str)

        for item in last_array:
            print(item)

    file.close()
    reports(f_check)
    
def report_2(f_check):

    """
    Функция report_2 формирует отчет о владельцах автомобилей указанной марки с использованием заданных ключей для сортировки.
    После сортировки результаты выводятся на экран.
    """

    year_rel_array = []
    volume_array = []
    surname_array = []

    try:
        n_brand = str(input('Введите название марки: '))
    except ValueError:
        print('Вы ввели некорректные данные, попробуйте ещё раз')
        return
    
    with open('data.txt', 'r', encoding="utf-8") as file:
        for line in file:
            line_data = line.split()
            if n_brand == str(line_data[4]):
                year_rel_array.append(int(line_data[6]))
                volume_array.append(float(line_data[5]))
                surname_array.append(str(line_data[0]))

    n = len(year_rel_array)
    if n == 0:
        print('Машин такой марки нет в базе данных')
    else:
        for i in range(n):
            for j in range(0, n-i-1):
                if year_rel_array[j] < year_rel_array[j+1]:
                    year_rel_array[j], year_rel_array[j+1] = year_rel_array[j+1], year_rel_array[j]
                    volume_array[j], volume_array[j+1] = volume_array[j+1], volume_array[j]
                    surname_array[j], surname_array[j+1] = surname_array[j+1], surname_array[j]

        for i in range(n):
            print(f"Год выпуска: {year_rel_array[i]}, Объём двигателя: {volume_array[i]}, Фамилия: {surname_array[i]}")

    file.close()
    reports(f_check)

def report_3(f_check):
    """
    Функция report_3 формирует отчет о владельцах автомобилей с заданным годом выпуска на основе ключей для сортировки.
    После сортировки результаты выводятся на экран.
    """    
    year_rel_dict = {}
    year_brand_array = []
    surname_array = []
    
    try:
        year_rel = int(input('Введите год, раньше которого вы хотите узнать: '))
        if year_rel < 1884:
            print('Слишком давно, попробуйте снова')
        else:
            break
    except ValueError:
        print('Вы ввели некорректные данные, попробуйте ещё раз')

    with open('data.txt', 'r', encoding="utf-8") as file:
        for line in file:
            data = line.split()
            if int(data[6]) < year_rel:
                year_brand_array.append((int(data[6]), data[4], data[0]))

    year_brand_array.sort(key=lambda x: (-x[0], x[1]))

    for item in year_brand_array:
        year = item[0]
        brand = item[1]
        surname = item[2]
        if year in year_rel_dict:
            year_rel_dict[year].append((surname, brand))
        else:
            year_rel_dict[year] = [(surname, brand)]

    for year, owners in year_rel_dict.items():
        owners_str = ' '.join([f'{owner[1]} {owner[0]}' for owner in sorted(owners)])
        print(f'{year} : {owners_str}')

    file.close()
    reports(f_check)
    
def database_view(f_check):

    "Функция database_view выводит всю базу данных из файла на экран"

    with open('data.txt', 'r+', encoding="utf-8") as file:

        lines = file.readlines()
        for i in range (len(lines)):
            print(lines[i])
        database(f_check)

def add_str_database(f_check):

    """
    Функция add_str_database позволяет добавить запись в базу данных.
    После ввода данных производит их проверку и сохранение в файл.
    """

    with open('data.txt', 'a', encoding="utf-8") as file:

        print('Если хотите продолжить ввод записи введите 1',
                '\nЕсли хотите вернутся к выбору действий с базой данных, введите 0',
                '\n',
                '\nПорядок ввода данных ФИО: фамилия, имя, отчество. В ФИО не должно быть ничего кроме букв',
                '\nРегистрационный номер имеет вид "одна буква"-"три цифры"-"две буквы".',
                '\nРазрешённые для использования заглавные буквы: (А, В, Е, К, М, Н, О, Р, С, Т, У, Х.)',
                '\nМарка записывается любыми символами.',
                '\nОбъём двигателя - Число, если оно дробное, то дробь пишется через точку',
                '\nГод выпуска - целое, четырёхзначное число не раньше 1884 и не позже 2024',
                '\nГод регистрации - целое, четырёхзначное число, не раньше 1993 и не позже 2024',
                '\nПример: Иванов Иван Иванович А123ВЕ Toyota 1.6 2018 2020',
                '\n ')
        
        try:
            choise_n = int(input('Введите число для выбора: '))
        except ValueError:
            print('Вы ввели некорректные данные, попробуйте ещё раз')
            add_str_database(f_check)
        else:
            if choise_n == 0:
                database(f_check)

            elif choise_n == 1:

                add_str = str(input('Напишите все данные разделяя пробелами, согласно примеру и инструкции: '))
                add_str_array = add_str.split()

                if len(add_str_array) != 8:
                    print('Вы ввели некорректную запись, попробуйте ещё раз')
                    file.close()
                    add_str_database(f_check)

                else:
                    check(add_str, f_check) 
                    add_str = add_str + '\n'
                    file.write(add_str)    
                    print('Добавление было произведено успешно')

            else:
                print('Вы ввели некорректные данные, попробуйте ещё раз')
                add_str_database(f_check)

    file.close()
    database(f_check)

def del_str_database(f_check):

    """
    Функция del_str_database позволяет пользователю удалить запись из базы данных.
    Осуществляет проверку вводимых данных и удаление выбранной записи.
    """

    print('Если хотите продолжить удаление записи введите 1',
            '\nЕсли хотите вернутся к выбору действий с базой данных, введите 0',
            '\n')
    try:
        choise_n = int(input('Введите число для выбора: '))
    except ValueError:
        print('Вы ввели некоректные данные, попробуйте ещё раз')
        del_str_database(f_check)
    else:
        if choise_n == 0:
            database(f_check)
        elif choise_n == 1:
            with open('data.txt', 'r', encoding="utf-8") as file:
                try:
                    change_str = int(input('Введите номер строки которую хотите удалить: '))
                except ValueError:
                    print('Вы ввели некорректные данные, попробуйте ещё раз')
                    del_str_database(f_check)
                else:
                    files = file.readlines()
                    if len(files) == 25:
                        print('Удаление записи приведёт к наличию менее 25 строк в БД, поэтому это невозможно')
                        database(0)
                    elif change_str < 1  and change_str >(len(files)+2):
                        print('Такой строки нет в БД')
                        database(0)
                    else:
                        del_el = files.pop(change_str-1)
                        print('Удаление произведено успешно')
            file.close()
            
            with open('data.txt', 'w+', encoding="utf-8") as file_sec:
                for i in range(0,len(files)):
                    file_sec.write(files[i])
            file_sec.close()
            database(f_check)

        else:
            print('Вы ввели некорректные данные, попробуйте снова')
            del_str_database(f_check)
    
def change_str_database(f_check):

    """
    Функция change_str_database позволяет пользователю изменить запись в базе данных.
    Выполняет проверку вводимых данных и изменение выбранной записи, если условия выполнены.
    """

    print('Если хотите продолжить изменение записи введите 1',
                '\nЕсли хотите вернутся к выбору действий с базой данных, введите 0',
                '\n')
    try:
        choise_n = int(input('Введите цифру для выбора: '))
    except ValueError:
        print('Вы ввели некоректные данные, попробуйте ещё раз')
        change_str_database(f_check)
    else:
        if choise_n == 0:
            database(f_check)
        elif choise_n == 1:
            with open('data.txt', 'r', encoding="utf-8") as file:
                files = file.readlines()
                try:
                    change_str_n = int(input('Введите номер строки которую хотите изменить: '))
                except ValueError:
                    print('Вы ввели некорректные данные, попробуйте ещё раз')
                    change_str_database(f_check)
                else:
                    if change_str_n < 1 and change_str_n >(len(files)+2):
                        print('Такой строки нет в БД')
                        database(0)
                    else:

                        print('Если хотите продолжить ввод записи введите 1',
                    '\nЕсли хотите вернутся к выбору действий с базой данных, введите 0',
                    '\nПорядок ввода данных ФИО: фамилия, имя, отчество. В ФИО не должно быть ничего кроме букв',
                    '\nРегистрационный номер имеет вид "одна буква"-"три цифры"-"две буквы".',
                    '\nРазрешённые для использования заглавные буквы: (А, В, Е, К, М, Н, О, Р, С, Т, У, Х.)',
                    '\nМарка записывается любыми символами.',
                    '\nОбъём двигателя - Число, если оно дробное, то дробь пишется через точку',
                    '\nГод выпуска - целое, четырёхзначное число не раньше 1884 и не позже 2024',
                    '\nГод регистрации - целое, четырёхзначное число, не раньше 1993 и не позже 2024',
                    '\nПример: Иванов Иван Иванович А123ВЕ Toyota 1.6 2018 2020',
                    '\n ')
            
                    try:
                        choise_n = int(input('Введите цифры для выбора: '))
                    except ValueError:
                        print('Вы ввели некорректные данные, попробуйте ещё раз')
                        change_str_database(f_check)
                    else:
                        if choise_n == 0:
                            database(f_check)

                        elif choise_n == 1:

                            change_str = str(input('Напишите все данные разделяя пробелами, согласно примеру и инструкции: '))
                            change_str_array = change_str.split()

                            if len(change_str_array) != 8:
                                print('Вы ввели некорректную запись, попробуйте ещё раз')
                                file.close()
                                change_str_database(f_check)

                            else:
                                check(change_str, 3)
                                if
                                files[change_str_n-1] = change_str + '\n'
                                print('Изменение произведено успешно')
                                change_str_database(f_check)
                            
                        else:
                            print('Вы ввели некорректные данные, попробуйте ещё раз')
                            change_str_database(f_check)

            file.close()
            
            with open('data.txt', 'w+', encoding="utf-8") as file_sec:
                for i in range(0,len(files)):
                    file_sec.write(files[i])
                file_sec.close()
        
        else:
            print('Вы ввели некорректные данные, попробуйте снова')
            change_str_database(f_check)

def check(data_str, f_check):

    """
    Функция check осуществляет проверку вводимых данных.
    Проверяет валидность введенных данных, таких как ФИО, регистрационный номер, объем двигателя и даты.
    При наличии ошибок ввода, возвращает сообщение об ошибке.
    """
    
    data_str = data_str.split()

    if len(data_str) == 8:

        try:
            n_surname = str(data_str[0])
            n_name = str(data_str[1])
            n_patronym = str(data_str[2])
            n_reg = str(data_str[3])
            brand = str(data_str[4])
            n_volume = float(data_str[5])
            year_rel_n = int(data_str[6])
            year_reg_n = int(str(data_str[7]))

        except ValueError:
            if  f_check == 1:
                return 2
            elif f_check == 0:
                print('Вы ввели некорректные данные, попробуйте ещё раз')
                add_str_database(f_check)

        else:
            if n_surname.isalpha() == False:
                if f_check == 1:
                    return 2
                elif f_check == 0:
                    print('В фамилии есть символы, которые не являются буквами, попробуйте ещё раз')
                    add_str_database(0)
                elif f_check == 3:
                    print('В фамилии есть символы, которые не являются буквами, попробуйте ещё раз')
                    change_str_database()

            if n_name.isalpha() == False:
                if f_check == 1:
                    return 2
                elif f_check == 0:
                    print('В имени есть символы, которые не являются буквами, попробуйте ещё раз')
                    add_str_database(0)
                elif f_check == 3:
                    print('В имени есть символы, которые не являются буквами, попробуйте ещё раз')
                    change_str_database()

            if n_patronym.isalpha() == False:
                if f_check == 1:
                    return 2
                elif f_check == 0:
                    print('В отчестве есть символы, которые не являются буквами, попробуйте ещё раз')
                    add_str_database(0)
                elif f_check == 3:
                    print('В отчестве есть символы, которые не являются буквами, попробуйте ещё раз')
                    change_str_database()

            if not((n_reg[0] in letters) and (n_reg[1] in numbers) and (n_reg[2] in numbers) and (n_reg[3] in numbers) and (n_reg[4] in letters) and (n_reg[5] in letters)):
                if f_check == 1:
                    return 2
                elif f_check == 0:
                    print('Введённая строка не соответствует форме, попробуйте ещё раз')
                    add_str_database(0)
                elif f_check == 3:
                    print('Введённая строка не соответствует форме, попробуйте ещё раз')
                    change_str_database()

            if year_rel_n < 1884 and year_rel_n > 2024:
                if  f_check == 1:
                    return 2
                elif f_check == 0:
                    print('Число вне допустимого диапазона')
                    add_str_database(0)
                elif f_check == 3:
                    print('Число вне допустимого диапазона')
                    change_str_database()

            elif year_rel_n < 1993 and year_rel_n > 2024:
                if  f_check == 1:
                    return 2
                elif f_check == 0:
                    print('Число вне допустимого диапазона')
                    add_str_database(0)
                elif f_check == 3:
                    print('Число вне допустимого диапазона')
                    change_str_database()            

    else:
        if f_check == 1:
            return 2
        elif f_check == 0:
            print('Вы ввели некорректные данные, попробуйте ещё раз')
            add_str_database(f_check)
        elif f_check == 3:
            print('Вы ввели некорректные данные, попробуйте ещё раз')
            change_str_database(0)

first_check(1)
