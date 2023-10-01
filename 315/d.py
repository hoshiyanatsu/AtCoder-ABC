#!/usr/bin/env python3
h, w = map(int, input().split())
cookies = [[char for char in input()] for _ in range(h)]
checked = [[False] * w for _ in range(h)]
# False→まだチェックされてない、True→行でチェックされた、-1→消えた
finish = False

while finish == False:
    copy_checked = checked.copy()
    for index_row, lst in enumerate(checked):
        all_same_row = True
        count_exist_row_cookies = lst.count(False)
        print(f"count_exist_row_cookies: {count_exist_row_cookies}")
        if count_exist_row_cookies > 1:
            false_indices = [i for i, value in enumerate(lst) if value == False]
            for j in range(len(false_indices) - 1):
                if (
                    cookies[index_row][false_indices[j]]
                    != cookies[index_row][false_indices[j + 1]]
                ):
                    all_same_row = False
                    break
        if all_same_row:
            checked[index_row] = [True for i in range(w) if i in false_indices]
    print(f"checked: {checked}")
    # ここまではOK
    for index_column in range(w):
        lst = [checked[i][index_column] for i in range(h)]
        all_same_column = True
        count_exist_column_cookies = h - lst.count(-1)
        print(f"count_exist_column_cookies: {count_exist_column_cookies}")
        if count_exist_column_cookies > 1:
            false_indices = [i for i, value in enumerate(lst) if value != -1]
            for j in range(len(false_indices) - 1):
                if cookies[j][index_column] != cookies[j + 1][index_column]:
                    all_same_column = False
                    break
            if all_same_column:
                for i in range(h):
                    if i in false_indices:
                        checked[i][index_column] = True

    checked = [[-1 if elem is True else elem for elem in lst] for lst in checked]
    # checked[index_column] = [-1 if elem is True else elem for elem in lst]
    if copy_checked == checked:
        finish = True
        break
    print(*checked)
print(sum(sublist.count(False) for sublist in checked))
