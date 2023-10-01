# s を出力してプログラムを終了
def Print(s):
    print(s)
    exit(0)

# 右に 90 度回転
def Rotate(v):
    w = [list(x) for x in v]
    for i in range(4):
        for j in range(4):
            w[3 - j][i] = v[i][j]
    v[:] = [''.join(row) for row in w]

# (i, j) がグリッド内部かを判定する
def in_grid(i, j):
    return 0 <= i < 4 and 0 <= j < 4

# p を (di, dj) を左上の位置として配置できるか？
def can_put(exist, p, di, dj):
    for i in range(4):
        for j in range(4):
            if p[i][j] == '#':
                ni = i + di
                nj = j + dj
                if not in_grid(ni, nj) or exist[ni][nj] == 1:
                    return False
                exist[ni][nj] = 1
    return True

# ポリオミノを再帰で置いていく関数
def dfs(i, exist, ps):
    if i == 3:
        ok = all(all(exist[u][v] == 1 for v in range(4)) for u in range(4))
        if ok:
            Print("Yes")
        return
    for di in range(-3, 4):
        for dj in range(-3, 4):
            ex2 = [row[:] for row in exist]
            flag = can_put(ex2, ps[i], di, dj)
            if flag:
                dfs(i + 1, ex2, ps)

if __name__ == "__main__":
    ps = []
    for _ in range(3):
        ps.append(['' for _ in range(4)])
        for i in range(4):
            ps[-1][i] = input()
    
    for t in range(4):
        for u in range(4):
            dfs(0, [[0] * 4 for _ in range(4)], ps)
            Rotate(ps[2])
        Rotate(ps[1])
    
    Print("No")
