a_list = [list(map(int, input().split())) for _ in range(9)]

def row_checker(a_list: list):
    for row in range(9):
        if len(a_list[row])!=len(set(a_list[row])):
            return False
    return True

def column_checker(a_list: list):
    for column in range(9):
        column_list = [a_list[row][column] for row in range(9)]
        if len(column_list)!=len(set(column_list)):
            return False
    return True

def block_checker(a_list: list):
    for row in range(3):
        for column in range(3):
            block_list = [a_list[3*row+i][3*column+j] for i in range(3) for j in range(3)]
            if len(block_list)!=len(set(block_list)):
                return False
    return True

if row_checker(a_list) and column_checker(a_list) and block_checker(a_list):
    print('Yes')
else:
    print('No')