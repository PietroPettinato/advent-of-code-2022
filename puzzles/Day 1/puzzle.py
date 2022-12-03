import numpy as np


######################################
##############  PART 1  ##############
######################################

# test_data = [1000, 2000, 3000, None, 4000, None, 5000, 6000, None, 7000, 8000, 9000, None, 10000]
input_data = []
with open('input.txt') as f:
    for line in f.readlines():
        if line.rstrip() == '':
            input_data.append(None)
        else:
            input_data.append(int(line.rstrip()))

i = 0
kcal = [0] * (input_data.count(None) + 1)
for f in input_data:
    if f is None:
        i += 1
    else:
        kcal[i] += f

kcal = np.array(kcal)
# print(kcal)
print('Elf with most calories: ', np.argmax(kcal))
print('Calories: ', kcal[np.argmax(kcal)])


######################################
##############  PART 2  ##############
######################################


kcal = np.sort(kcal)[::-1]
tot = kcal[0] + kcal[1] + kcal[2]
print('Tot Calories of the three elfs: ', tot)

