# Задача 5.Устройство состоит из трех деталей. Для первой детали вероятность выйти из строя в первый месяц равна 0.1, для второй - 0.2, для третьей - 0.25. 
# Какова вероятность того, что в первый месяц выйдут из строя: а). все детали б). только две детали в). хотя бы одна деталь г). от одной до двух деталей?

ver_1detail_break = 0.1
ver_2detail_break = 0.2
ver_3detail_break = 0.25

ver_all_break = ver_1detail_break * ver_2detail_break * ver_3detail_break
print("Вероятность, что в первый месяц выйдут из строя все детали", ver_all_break)

ver_only_two = ver_1detail_break * ver_2detail_break * (1 - ver_3detail_break) + ver_1detail_break * (1 - ver_2detail_break) * ver_3detail_break + (1 - ver_1detail_break) * ver_2detail_break * ver_3detail_break
print("Вероятность, что в первый месяц выйдут из строя только две детали", ver_only_two)

ver_one_of_all = 1 - (1 - ver_1detail_break ) * (1 - ver_2detail_break) * (1 - ver_3detail_break)
print("Вероятность, что в первый месяц выйдет из строя хотя бы одна деталь", ver_one_of_all)

ver_only_one = ver_1detail_break * ( 1 - ver_2detail_break) * (1 - ver_3detail_break) + (1 - ver_1detail_break) * ver_2detail_break * (1 - ver_3detail_break) + (1 - ver_1detail_break) * (1 - ver_2detail_break) * ver_3detail_break

ver_one_or_two = ver_only_two + ver_only_one
print("Вероятность, что в первый месяц выйдет из строя от одной до двух деталей", ver_one_or_two)

#или 
#ver_one_or_two = ver_one_of_all - ver_all_break
#print("Вероятность, что в первый месяц выйдет из строя от одной до двух деталей", ver_one_or_two)