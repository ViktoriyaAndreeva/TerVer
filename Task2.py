# Задача 2. В первом ящике находится 8 мячей, из которых 5 - белые. Во втором ящике - 12 мячей, из которых 5 белых.
# Из первого ящика вытаскивают случайным образом два мяча, из второго - 4. Какова вероятность того, что 3 мяча белые?

box1 = 8
white_box1 = 5
box2 = 12
white_box2 = 5
n1 = 2
n2 = 4

ver_white_box1 = white_box1 / box1
ver_not_white_box1 = (box1 - white_box1) / box1
ver_white_box2 = white_box2 / box2
ver_not_white_box2 = (box2 - white_box2) / box2
result_three_white = ver_white_box1*4/7*ver_white_box2*7/11*6/10*5/9 + ver_white_box1 * \
    3/7*ver_white_box2*4/11*7/10*6/9 + \
    ver_not_white_box1*2/7*ver_white_box2*4/11*3/10*7/9
print("Вероятность, что 3 мяча белые:", result_three_white)
