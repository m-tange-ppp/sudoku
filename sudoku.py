import random as rd

#盤面を表示
def show(A):
    print("-----------------")
    for a in A:
        print(*a)
    print("-----------------")

#盤面が数独の規則を満たしているか判定
def check_board(A):
    nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    for i in range(9):
        r = set()
        for j in range(9):
            r.add(A[i][j])
        if r != nums:
            return False
    
    for j in range(9):
        c = set()
        for i in range(9):
            c.add(A[i][j])
        if c != nums:
            return False
    
    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            s = set()
            for k in range(i, i + 3):
                for l in range(j, j + 3):
                    s.add(A[k][l])
            if s != nums:
                return False
    return True

#上中下それぞれの正方形グループが規則を満たすか判定
def check_row_square(A, r):
    nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    for j in range(0, 7, 3):
        s = set()
        for k in range(r, r + 3):
            for l in range(j, j + 3):
                s.add(A[k][l])
        if s != nums:
            return False
    return True

#規則を満たす盤面を個数して生成
def generate_board(c):
    count = 0
    maxij = 0
    B = []
    nums = [i for i in range(1, 10)]
    while count < c:
        board = [[0] * 9 for _ in range(9)]
        for i in range(9):
            if i == 0:
                rd.shuffle(nums)
                for j in range(9):
                    board[i][j] = nums[j]
            else:
                while True:
                    rd.shuffle(nums)
                    for j in range(9):
                        for k in range(i):
                            if board[k][j] == nums[j]:
                                break
                        else:
                            continue
                        break
                    else:
                        for j in range(9):
                            board[i][j] = nums[j]
                        break
            row_square_ok = True
            if (i == 2 or i == 5 or i == 8) and j == 8:
                if not check_row_square(board, i - 2):
                    row_square_ok = False
            if row_square_ok:
                if maxij < 10 * i + j:
                    maxij = 10 * i + j
                    show(board)
                    print("完成品↑" if i == 8 and j == 8 else "過去一惜しいやつ↑")
                continue
            break
        else:
            B.append(board)
            maxij = 0
            count += 1
    return B


A1 = [[1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9]]
A2 = [[1,2,3,4,5,6,7,8,9],
    [4,5,6,7,8,9,1,2,3],
    [7,8,9,1,2,3,4,5,6],
    [2,3,4,5,6,7,8,9,1],
    [5,6,7,8,9,1,2,3,4],
    [8,9,1,2,3,4,5,6,7],
    [3,4,5,6,7,8,9,1,2],
    [6,7,8,9,1,2,3,4,5],
    [9,1,2,3,4,5,6,7,8]]

show(A1)
print("Yes" if check_board(A1) else "No")
print("Yes" if check_row_square(A1, 0) else "No")
show(A2)
print("Yes" if check_board(A2) else "No")
print("Yes" if check_row_square(A2, 3) else "No")

for b in generate_board(int(input("1つ3分くらいかかるけどいくつ作る？"))):
    show(b)
    print("Yes" if check_board(b) else "No")