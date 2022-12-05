import pandas as pd


######################################
##############  PART 1  ##############
######################################

def is_fully_contained(s1, s2):
    a1 = s1.split('-')
    a2 = s2.split('-')
    if int(a2[0]) in range(int(a1[0]), int(a1[1])+1) and int(a2[1]) in range(int(a1[0]), int(a1[1])+1):
        return True
    elif int(a1[0]) in range(int(a2[0]), int(a2[1])+1) and int(a1[1]) in range(int(a2[0]), int(a2[1])+1):
        return True
    return False

df = pd.read_csv(filepath_or_buffer='input.csv', names=['assignment 1', 'assignment 2'])
print(df)

df['fully contained'] = df.apply(lambda x: is_fully_contained(x['assignment 1'], x['assignment 2']), axis=1)
print(df)
print('Assignments that fully contains the other:', df['fully contained'].sum())


######################################
##############  PART 2  ##############
######################################

def is_contained(s1, s2):
    a1 = s1.split('-')
    a2 = s2.split('-')
    if int(a2[0]) in range(int(a1[0]), int(a1[1])+1) or int(a2[1]) in range(int(a1[0]), int(a1[1])+1):
        return True
    elif int(a1[0]) in range(int(a2[0]), int(a2[1])+1) or int(a1[1]) in range(int(a2[0]), int(a2[1])+1):
        return True
    return False


df['overlap'] = df.apply(lambda x: is_contained(x['assignment 1'], x['assignment 2']), axis=1)
print(df)
print('Assignments that overlap the other:', df['overlap'].sum())
