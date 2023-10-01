n, m = map(int, input().split())
s = list(input())
li_c = list(map(int, input().split()))

temp_s = s.copy()

# li_li_index = [
#     [index for index, value in enumerate(li_c) if value == i + 1] for i in range(m)
# ]
# for index, li_index in enumerate(li_li_index):
#     if len(li_index) > 1:
#         for idx, value in enumerate(li_index):
#             if idx == 0:
#                 s[value] = temp_s[li_index[-1]]

#             else:
#                 s[value] = temp_s[li_index[idx - 1]]

# print("".join(s))

# 各色のインデックスを集計
color_indices = [[] for _ in range(m)]
for idx, value in enumerate(li_c):
    color_indices[value - 1].append(idx)

# 操作を実行
for indices in color_indices:
    if len(indices) >= 2:
        last_char = s[indices[-1]]  # 最後の文字を保存
        for i in range(len(indices)):
            temp = s[indices[i]]
            s[indices[i]] = last_char
            last_char = temp

result = "".join(s)
print(result)
