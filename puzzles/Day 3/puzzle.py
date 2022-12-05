import numpy as np
import pandas as pd
import string


######################################
##############  PART 1  ##############
######################################


def find_common_item(s):
    i1 = s[:int(len(s) / 2)]
    i2 = s[int(len(s) / 2):]
    for c in list(i2):
        try:
            list(i1).index(c)
            return c
        except ValueError:
            pass


df = pd.read_csv(filepath_or_buffer='input.csv', names=['rucksack'])
print(df)

'''
Lowercase item types a through z have priorities 1 through 26.
Uppercase item types A through Z have priorities 27 through 52.
'''

vals_low = list(range(1, 27))
low_alphabet = list(string.ascii_lowercase)
priorities = {low_alphabet[i]: vals_low[i] for i in range(len(low_alphabet))}

vals_upp = list(range(27, 53))
upp_alphabet = list(string.ascii_uppercase)
priorities.update({upp_alphabet[i]: vals_upp[i] for i in range(len(upp_alphabet))})

df['common item'] = [find_common_item(row) for row in df['rucksack']]
df['priority value'] = [priorities[i] for i in df['common item']]

print('Sum of priorities: ', df['priority value'].sum())


######################################
##############  PART 2  ##############
######################################


def find_badges(df):
    badge = []
    for i in range(0, len(df), 3):
        vals = df['rucksack'][i:i + 3].values
        inters = set(vals[0]).intersection(vals[1]).intersection(vals[2])
        badge.extend(inters)
    return badge


tot = np.array([priorities[i] for i in find_badges(df)]).sum()
print('Sum of priorities of badges: ', tot)

