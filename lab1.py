file = open("sport.txt", encoding="cp1251")
header = file.readline()
stat_dict = dict()
for i in file.readlines():
    sport = i.split('\t')[3].split(',')
    if len(sport) != 0:
        for sport_i in sport:
            if sport_i in stat_dict: stat_dict[sport_i] += 1
            else: stat_dict[sport_i] = 1
flag = 3
print("Самые популярные виды спорта в стране: ")
counter = 1
for i in sorted(stat_dict.items(), reverse=True, key=lambda x:x[1]):
    if len(i[0]) != 0:
        print(f'{counter}) {i[0]}')
        counter += 1
    if counter == 4:
        exit()

