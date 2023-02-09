T = int(input())

for tc in range(1, T+1):
    A = input()

    A = A.replace('()', '1')

    total = 0
    s_cnt = 0
    m_cnt = 0

    for i in range(len(A)):
        if A[i] == '(':
            s_cnt += 1
            total += 1
        elif A[i] == ')':
            s_cnt -= 1
        else:
            m_cnt += s_cnt

    print(m_cnt+total)