import sys

def stack(ps_list, ps):
    vps = 'YES'
    for p in ps:
        if p == '(':
            ps_list.append(p)
        else:
            if len(ps_list) == 0:
                return 'NO'
            ps_list.pop()

    if len(ps_list) == 0:
        return 'YES'

    return 'NO'

T = int(input())

for _ in range(T):
    ps_list = []
    ps = list(sys.stdin.readline().strip())
    vps = stack(ps_list, ps)
    print(vps)
