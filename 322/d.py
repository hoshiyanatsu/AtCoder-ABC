def main(p1_matrix:list, p2_matrix:list, p3_matrix:list):
    p1_count_polymino = count_polyomino(matrix=p1_matrix)
    p2_count_polymino = count_polyomino(matrix=p2_matrix)
    p3_count_polymino = count_polyomino(matrix=p3_matrix)
    if (p1_count_polymino+p2_count_polymino+p3_count_polymino)!=16:
        # そもそも個数的に満たし得ないときはFalseを返す
        return False
    
    down_list = [-3, -2, -1, 0, 1, 2, 3]
    right_list = [-3, -2, -1, 0, 1, 2, 3]

    for _ in range(4):
        for _ in range(4):
            for _ in range(4):
                if get_avaliable(p1=p1_matrix, p2=p2_matrix, p3=p3_matrix):
                    return True
                for d in down_list:
                    for r in right_list:
                        try:
                            p3_matrix = parallel_move(down=d, right=r, matrix=p3_matrix)
                        except:
                            continue
                p3_matrix=right_rotate(matrix=p3_matrix)
            for d in down_list:
                for r in right_list:
                    try:
                        p2_matrix = parallel_move(down=d, right=r, matrix=p2_matrix)
                    except:
                        continue
            p2_matrix=right_rotate(matrix=p2_matrix)
        for d in down_list:
            for r in right_list:
                try:
                    p1_matrix = parallel_move(down=d, right=r, matrix=p1_matrix)
                except:
                    continue
        p1_matrix=right_rotate(matrix=p1_matrix)
    return False

def count_polyomino(matrix):
    count = 0
    for i in range(4):
        for j in range(4):
            if matrix[i][j]=="#":
                count+=1
    return count


def parallel_move(down:int, right:int, matrix:list):
    """
    与えられただけmatrixを下にdown分、右にright分だけ動かす
    """
    moved_list = [["" for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            moved_list[i+down][j+right] = matrix[i][j]
    return moved_list


def right_rotate(matrix:list):
    """
    右に90度回転
    """
    rotated_list = [["" for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            rotated_list[j][3-i]= matrix[i][j]
    return rotated_list


def get_avaliable(p1:list, p2:list, p3:list):
    for i in range(4):
        for j in range(4):
            if p1[i][j]=="." and p2[i][j]=="." and p3[i][j]==".":
                return False
    return True

if __name__=="__main__":
    p1_matrix = [list(input()) for _ in range(4)]
    p2_matrix = [list(input()) for _ in range(4)]
    p3_matrix = [list(input()) for _ in range(4)]
    ans = main(p1_matrix=p1_matrix, p2_matrix=p2_matrix, p3_matrix=p3_matrix)
    if ans:
        print("Yes")
    else:
        print("No")