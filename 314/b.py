n = int(input())
li_c = ["" for _ in range(n)]
li_a = ["" for _ in range(n)]
for i in range(n):
    li_c[i] = int(input())
    li_a[i] = list(map(int, input().split()))
x = int(input())

in_x = [False for _ in range(n)]

for i in range(n):
    if x in li_a[i]:
        in_x[i] = True


in_x_index = [i for i, value in enumerate(in_x) if value]
in_x_count = [li_c[i] for i in in_x_index]
minimum = 0
if len(in_x_count) > 0:
    minimum = min(in_x_count)
number_of_people = 0
li_answer = []
for i, value in enumerate(in_x):
    if value == True and li_c[i] == minimum:
        number_of_people += 1
        li_answer.append(i + 1)

print(number_of_people)
print(*li_answer)

# n = int(input())

# in_x_indices = []  # xが含まれる行のインデックスを保持
# minimum = float("inf")
# number_of_people = 0

# for i in range(n):
#     c = int(input())
#     a = list(map(int, input().split()))

#     if x in a:
#         in_x_indices.append(i)
#         minimum = min(minimum, c)

# for idx in in_x_indices:
#     if li_c[idx] == minimum:
#         number_of_people += 1

# print(number_of_people)

# for idx in in_x_indices:
#     if li_c[idx] == minimum:
#         print(idx + 1, end=" ")
# print()
