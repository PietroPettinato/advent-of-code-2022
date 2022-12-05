import pandas as pd


######################################
##############  PART 1  ##############
######################################


# test_data
# df = pd.DataFrame(data=[('A', 'Y'), ('B', 'X'), ('C', 'Z')], columns=['opponent', 'me'])

df = pd.read_csv(filepath_or_buffer='input.csv', header=0, sep=' ')
# print(df)

'''
opponent: A for Rock, B for Paper, and C for Scissors.
me      : X for Rock, Y for Paper, and Z for Scissors.
'''
round_points = {
    'AX': 3,  # D
    'AY': 6,  # W
    'AZ': 0,  # L

    'BX': 0,  # L
    'BY': 3,  # D
    'BZ': 6,  # W

    'CX': 6,  # W
    'CY': 0,  # L
    'CZ': 3   # D
}

shape_points = {
    'A': 1,
    'X': 1,
    'B': 2,
    'Y': 2,
    'C': 3,
    'Z': 3
}


concat = pd.Series(df['opponent'] + df['me'])
df['round points'] = [round_points[r] for r in concat]
df['shape points'] = [shape_points[r] for r in df['me']]
df['tot points'] = df['round points'] + df['shape points']
print(df)
print('Tot points for all rounds: ', df['tot points'].sum())




######################################
##############  PART 2  ##############
######################################

'''
X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.

    In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also 
    choose Rock. This gives you a score of 1 + 3 = 4. 

    In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score 
    of 1 + 0 = 1.

    In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7. 

    Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.
'''

round_points = {
    'X': 0,  # L
    'Y': 3,  # D
    'Z': 6,  # W
}

shape_points = {
    'AX': 3,  # S
    'AY': 1,  # R
    'AZ': 2,  # P

    'BX': 1,  # R
    'BY': 2,  # P
    'BZ': 3,  # S

    'CX': 2,  # P
    'CY': 3,  # S
    'CZ': 1   # R
}

shape_points2 = {
    'AX': 'C',  # S
    'AY': 'A',  # R
    'AZ': 'B',  # P

    'BX': 'A',  # R
    'BY': 'B',  # P
    'BZ': 'C',  # S

    'CX': 'B',  # P
    'CY': 'C',  # S
    'CZ': 'A'   # R
}

shape_points3 = {
    'A': 1, # Rock
    'B': 2, # Paper
    'C': 3  # Scissors
}


df = pd.read_csv(filepath_or_buffer='input.csv', header=0, sep=' ')

df['round points'] = [round_points[r] for r in df['me']]
concat = pd.Series(df['opponent'] + df['me'])
df['shape points'] = [shape_points[r] for r in concat]
df['tot points'] = df['round points'] + df['shape points']
print(df)
print('Tot points for all rounds: ', df['tot points'].sum())

