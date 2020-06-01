t = int(input())

for i in range(0, t):
    r, c = input().split()
    r, c = int(r), int(c)
    a = input().split()[0:r * c]
    A = []
    for x in range(0, r):
        B = []
        for y in range(0, c):
            B.append(int(a[0]))
            a.pop(0)
        A.append(B)
    p = [0, 2]
    flag = 0
    while flag != -1:
        C = []
        count = 0

        for v in range(0, r):
            for u in range(0, c):
                if A[v][u] == 2:
                    C.append([v, u])
        while (C):
            x, y = C[0]

            if 1 <= x <= r-2 and 1 <= y <= c - 2:
                if A[x - 1][y] not in p:
                    A[x - 1][y] = 2
                    count = 1
                if A[x + 1][y] not in p:
                    A[x + 1][y] = 2
                    count = 1
                if A[x][y + 1] not in p:
                    A[x][y + 1] = 2
                    count = 1
                if A[x][y - 1] not in p:
                    A[x][y - 1] = 2
                    count = 1

            elif x == 0 and y == 0:
                if A[x + 1][y] not in p:
                    A[x + 1][y] = 2
                    count = 1
                if A[x][y + 1] not in p:
                    A[x][y + 1] = 2
                    count = 1

            elif x == 0 and y == c - 1:
                if A[x + 1][y] not in p:
                    A[x + 1][y] = 2
                    count = 1

                if A[x][y - 1] not in p:
                    A[x][y - 1] = 2
                    count = 1

            elif y == 0 and x == r - 1:
                if A[x - 1][y] not in p:
                    A[x - 1][y] = 2
                    count = 1

                if A[x][y + 1] not in p:
                    A[x][y + 1] = 2
                    count = 1

            elif x == r - 1 and y == c - 1:
                if A[x - 1][y] not in p:
                    A[x - 1][y] = 2
                    count = 1

                if A[x][y - 1] not in p:
                    A[x][y - 1] = 2
                    count = 1

            elif x == 0 and y <= c - 2:
                if A[x + 1][y] not in p:
                    A[x + 1][y] = 2
                    count = 1

                if A[x][y - 1] not in p:
                    A[x][y - 1] = 2
                    count = 1

                if A[x][y + 1] not in p:
                    A[x][y + 1] = 2
                    count = 1

            elif y == 0 and x <= r - 2:
                if A[x + 1][y] not in p:
                    A[x + 1][y] = 2
                    count = 1

                if A[x - 1][y] not in p:
                    A[x - 1][y] = 2
                    count = 1

                if A[x][y + 1] not in p:
                    A[x][y + 1] = 2
                    count = 1

            elif x == r - 1 and y <= c - 2:
                if A[x - 1][y] not in p:
                    A[x - 1][y] = 2
                    count = 1

                if A[x][y + 1] not in p:
                    A[x][y + 1] = 2
                    count = 1

                if A[x][y - 1] not in p:
                    A[x][y - 1] = 2
                    count = 1

            elif y == c - 1 and x <= r - 2:
                if A[x + 1][y] not in p:
                    A[x + 1][y] = 2
                    count = 1

                if A[x - 1][y] not in p:
                    A[x - 1][y] = 2
                    count = 1

                if A[x][y - 1] not in p:
                    A[x][y - 1] = 2
                    count = 1
            #     if A[x + 1][y] not in p:
            #         A[x + 1][y] = 2
            #         count = count + 1
            #
            #     if A[x - 1][y] not in p:
            #         A[x - 1][y] = 2
            #         count = count + 1
            #
            #     if A[x][y - 1] not in p:
            #         A[x][y - 1] = 2
            #         count = count + 1
            #     if A[x][y + 1] not in p:
            #         A[x][y + 1] = 2
            #         count = count + 1
            C.pop(0)
        print(count)
        if count != 0:
            flag = flag+1
        else:
            count = flag
            flag = -1
        print(flag)
    print(A)
    for v in range(0, r):
        for u in range(0, c):
            if A[v][u] == 1:
                count = -1
    print(count)
