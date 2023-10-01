def find_kth_321_like_number(K):
    current_number = 1  # 現在の321-like Number
    count = 1  # 321-like Numberの数をカウント

    while count < K:
        found = False
        current_number += 1
        digits = list(str(current_number))

        for i in range(1, len(digits)):
            if digits[i] > digits[i - 1]:
                continue  # 条件を満たさない場合、次の数を試す

        # 条件を満たす場合、321-like Numberを見つけた
        count += 1

    return current_number

# Kを入力として受け取り、K番目の321-like Numberを求める
K = int(input())
result = find_kth_321_like_number(K)
print(result)
