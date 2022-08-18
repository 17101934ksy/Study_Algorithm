import sys

def stack(line):
    line_list = []
    vline = 'yes'
    for p in line:
        if p in ['(', ')', '[', ']']:
            if p in ['(','[']:
                line_list.append(p)
            else:
                if len(line_list) == 0:
                    return 'no'
                else:
                    p_pop = line_list.pop()
                    if p == ')':
                        if p_pop != '(':
                            return 'no'
                    elif p == ']':
                        if p_pop != '[':
                            return 'no'

    if len(line_list) == 0:
        return vline
    return 'no'

lines = ''
while True:
    line = sys.stdin.readline()   
    if line == '.\n':
        break
    lines += line

lines = lines.split('.')

for line in lines[:-1]:
    vline = stack(line)
    print(vline)