import matplotlib.pyplot as plt
from fnmatch import fnmatch
sr_pens = []
dates = []
try:
    file = open('opendata.stat.txt')
    file.readline()
    for i in file.readlines():
        try:
            name, region, date,  value = i.split(',')
        except ValueError:
            print("Ошибка! Недостаточно данных")
            continue
        if region == "Забайкальский край":
            if fnmatch(date, "2018-??-??"):
                if name == 'Средняя пенсия':
                    try:
                        sr_pens.append(int(value))
                        dates.append(date)
                    except ValueError:
                        print(f"Ошибка! Некорректные данные: {value}")
    file.close()
    print(f"Средняя пенсия в Забайкальском крае равна {sum(sr_pens)/12}")
except FileNotFoundError:
    print("Ошибка! Файл не найден")
except PermissionError:
    print("Ошибка доступа к файлу!")

plt.figure(figsize=(14, 6))
plt.plot(dates, sr_pens, color='green', marker='o', markersize=7)
plt.xlabel('Дата')
plt.ylabel('Размер пенсии, руб')
plt.title('График изменения пенсии в Забайкальском крае в 2018 году')
plt.show()