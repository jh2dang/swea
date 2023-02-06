T = int(input())

for i in range(1, T + 1):
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))

    # print(charge)  # 찍어보기

    stop = [0] * (N + K+1)

    for num in charge:
        stop[num] = 1

    # print(stop)  # 찍어보기

    cnt = 0
    me = 0

    Flag = False

    while me+K < N:
        for j in range(me + K, me, -1):
            if stop[j] == 1:
                me = j
                cnt += 1
                break
            else:
                pass
        else:
            Flag = True

        if Flag:
            break
    if Flag:
        print(f'#{i} 0')
    else:
        print(f'#{i} {cnt}')