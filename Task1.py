#Задача 1. Даны значения зарплат из выборки выпускников: 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150. 
#Посчитать (желательно без использования статистических методов наподобие std, var, mean) среднее арифметическое, среднее квадратичное отклонение, смещенную и несмещенную оценки дисперсий для данной выборки.

import numpy as np

array = np.array([100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150])
lenght_array = len(array)

print("Длина массива:", lenght_array)
result_first = sum(array) / lenght_array
print("Среднее арифметическое:", result_first)
array_minus_sr = (array - result_first)**2
summa_otkl = sum(array_minus_sr)
sm_disp = summa_otkl / lenght_array 
result_dispers = np.sqrt(sm_disp)
print("Среднее квадратичное отклонение:", result_dispers)
print("Смещенная дисперсия:", sm_disp )
nesm_disp = summa_otkl / (lenght_array - 1) 
print("Несмещенная дисперсия:", nesm_disp )
