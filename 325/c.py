def main(s_list:list, h:int, w:int):
    checked_list = [[False for _ in range(w)] for _ in range(h)] # True: checked, False: not checked
    counter = 0
    for i, s in enumerate(s_list):
        for j, x in enumerate(s):
            if checked_list[i][j] == False and x == "#":
                if i != h-1 and j != 0 and checked_list[i+1][j-1]:
                    pass
                else:
                    counter += 1
                checked_list = check(checked_list, i, j, s_list, h, w)
            checked_list[i][j] = True
            # print(checked_list)
    print(counter)

def check(checked_list:list, i:int, j:int, s_list:list, h:int, w:int):
    """
    i, j が "#" だったときに、どこまで繋がってるのか確かめて繋がりが切れたらchecked_listを返す。
    """
    before_i, before_j = i, j
    next_i, next_j = -1, -1
    on_down = False
    on_right = False
    on_right_down = False
    on_left_down = False
    while True:
        if not on_down:
            on_down = sensor_on_down(s_list, i, j, h, w)
            if on_down:
                next_i, next_j = i+1, j
        
        elif not on_right:
            on_right = sensor_on_right(s_list, i, j, h, w)
            if on_right:
                next_i, next_j = i, j+1
        
        elif not on_right_down:
            on_right_down = sensor_on_right_donw(s_list, i, j, h, w)
            if on_right_down:
                next_i, next_j = i+1, j+1
        
        elif not on_left_down:
            on_left_down = sensor_on_left_down(s_list, i, j, h, w)
            if on_left_down:
                next_i, next_j = i+1, j-1
        if next_i != i and next_j != j:
            on_down = False
            on_right = False
            on_right_down = False
            on_left_down = False
        else:
            i, j = before_i, before_j
        print(f"next_i:{next_i}, next_j:{next_j}")
        if next_i == i and next_j == j:
            break
        checked_list[next_i][next_j] = True
        before_i, before_j = i, j
        i, j = next_i, next_j
        
    
    return checked_list

def sensor_on_down(s_list:list, i:int, j:int, h:int, w:int):
    if i != h-1 and s_list[i+1][j] == "#":
        return True
    return False

def sensor_on_right(s_list:list, i:int, j:int, h:int, w:int):
    if j != w-1 and s_list[i][j+1] == "#":
        return True
    return False

def sensor_on_right_donw(s_list:list, i:int, j:int, h:int, w:int):
    if i != h-1 and j != w-1 and s_list[i+1][j+1] == "#":
        return True
    return False

def sensor_on_left_down(s_list:list, i:int, j:int, h:int, w:int):
    if i != h-1 and j != 0 and s_list[i+1][j-1] == "#":
        return True
    return False

    
if __name__=="__main__":
    h, w = map(int, input().split())
    s_list = [list(input()) for _ in range(h)]
    main(s_list=s_list, h=h, w=w)