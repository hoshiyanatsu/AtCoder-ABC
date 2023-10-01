def check_day(n, k, medicines):
    left = 1
    right = 10**18

    while left < right:
        mid = (left + right) // 2
        count = 0

        for a, b in medicines:
            if a > mid:
                continue
            count += (mid - a) // b + 1

        if count >= k:
            right = mid
        else:
            left = mid + 1

    return left


# 入力を受け取る
n, k = map(int, input().split())
medicines = []

for _ in range(n):
    a, b = map(int, input().split())
    medicines.append((a, b))

# 関数を呼び出して結果を出力
result = check_day(n, k, medicines)
print(result)
