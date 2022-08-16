import sys

N_list = [i for i in range(1, int(sys.stdin.readline())+1)]

if N_list == [1]:
    print(N_list[0])

else:
    for idx, i in enumerate(N_list):
        if (idx+1) % 2 == 0:
            N_list.append(i)

        if N_list[-2] == N_list[-1]:
            break
    print(N_list[-1])
