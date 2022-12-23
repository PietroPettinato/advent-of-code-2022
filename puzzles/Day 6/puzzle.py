
######################################
##############  PART 1  ##############
######################################

def subroutine(s, l):
    for i in range(len(s)):
        x = set(s[i:i + l])
        if len(x) == l:
            return i + l
    return None


with open('input.txt') as f:
    for line in f.readlines():
        print(subroutine(line, 4))
f.close()

######################################
##############  PART 2  ##############
######################################

with open('input.txt') as f:
    for line in f.readlines():
        print(subroutine(line, 14))
f.close()
