# #first_assignment
random1 = int(input('n = '))
biggest_number = 1
square_list = []
while biggest_number ** 2 <= random1:
    square_list.append(biggest_number ** 2)
    biggest_number += 1
print(square_list)
#second_assignment
random2 = int(input('k = '))
two_with_power = 2
power = 1
while two_with_power <= random2:
    two_with_power *= 2
    power += 1
print(power - 1, two_with_power // 2)
# third_assignment
len = 0
while int(input('m =')) != 0:
    len += 1
print(len)
