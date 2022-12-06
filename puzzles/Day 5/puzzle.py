from pprint import pprint


######################################
##############  PART 1  ##############
######################################

'''
------ INITIAL CONFIGURATIONS ------
[P]     [C]         [M]            
[D]     [P] [B]     [V] [S]        
[Q] [V] [R] [V]     [G] [B]        
[R] [W] [G] [J]     [T] [M]     [V]
[V] [Q] [Q] [F] [C] [N] [V]     [W]
[B] [Z] [Z] [H] [L] [P] [L] [J] [N]
[H] [D] [L] [D] [W] [R] [R] [P] [C]
[F] [L] [H] [R] [Z] [J] [J] [D] [D]
 1   2   3   4   5   6   7   8   9 
'''

stack = {
    '1': ['F', 'H', 'B', 'V', 'R', 'Q', 'D', 'P'],
    '2': ['L', 'D', 'Z', 'Q', 'W', 'V'],
    '3': ['H', 'L', 'Z', 'Q', 'G', 'R', 'P', 'C'],
    '4': ['R', 'D', 'H', 'F', 'J', 'V', 'B'],
    '5': ['Z', 'W', 'L', 'C'],
    '6': ['J', 'R', 'P', 'N', 'T', 'G', 'V', 'M'],
    '7': ['J', 'R', 'L', 'V', 'M', 'B', 'S'],
    '8': ['D', 'P', 'J'],
    '9': ['D', 'C', 'N', 'W', 'V']
}

pprint(stack)

with open('input.txt') as f:
    for line in f.readlines():
        line = line.split()
        move = line[1]
        from_stack = line[3]
        to_stack = line[-1]
        for i in range(int(move)):
            crate = stack[from_stack].pop()
            stack[to_stack].append(crate)
        # print(line)
        # pprint(stack)
f.close()

pprint(stack)
print('\nThe letters on the top of each stack are: JDTMRWCQJ\n')


######################################
##############  PART 2  ##############
######################################


# reinitialize configuration

stack = {
    '1': ['F', 'H', 'B', 'V', 'R', 'Q', 'D', 'P'],
    '2': ['L', 'D', 'Z', 'Q', 'W', 'V'],
    '3': ['H', 'L', 'Z', 'Q', 'G', 'R', 'P', 'C'],
    '4': ['R', 'D', 'H', 'F', 'J', 'V', 'B'],
    '5': ['Z', 'W', 'L', 'C'],
    '6': ['J', 'R', 'P', 'N', 'T', 'G', 'V', 'M'],
    '7': ['J', 'R', 'L', 'V', 'M', 'B', 'S'],
    '8': ['D', 'P', 'J'],
    '9': ['D', 'C', 'N', 'W', 'V']
}

pprint(stack)

with open('input.txt') as f:
    for line in f.readlines():
        line = line.split()
        move = line[1]
        from_stack = line[3]
        to_stack = line[-1]

        crate = []
        for i in range(int(move)):
            crate.insert(0, stack[from_stack].pop())
        [stack[to_stack].append(c) for c in crate]

        # print(line)
        # pprint(stack)

f.close()

pprint(stack)
print('\nThe letters on the top of each stack are: VHJDDCWRD')

