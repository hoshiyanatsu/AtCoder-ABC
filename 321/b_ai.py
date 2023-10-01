def find_minimum_score(N, X, A):
    min_score = min(A)
    max_score = max(A)
    remaining_sum = X + (N - 2) * min_score

    if remaining_sum <= 0:
        return -1
    elif remaining_sum + min_score > 100:
        return 100
    else:
        return remaining_sum

# 入力を受け取る
N, X = map(int, input().split())
A = list(map(int, input().split()))

result = find_minimum_score(N, X, A)
print(result)
