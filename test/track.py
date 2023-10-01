import sys


def main():
    input_list = input().split()
    n = int(input_list[0])
    m = int(input_list[1])

    power_dict = {}
    cost_dict = {}
    for i in range(1, n + 1):
        power_dict[i] = int(input_list[2 * i])
        cost_dict[i] = int(input_list[2 * i + 1])
    sorted_cost_list = sorted(cost_dict.items(), key=lambda pair: pair[1], reverse=True)
    power_sum_list = [0]

    # 以下の処理関数化して繰り返す
    for j in range(n):
        cost_sum = 0
        power_sum = 0
        while cost_sum < m + 1 and j < n:
            key = sorted_cost_list[j][0]
            cost = sorted_cost_list[j][1]
            if cost_sum + cost > m:
                j += 1
            else:
                cost_sum += cost
                power_sum += power_dict[key]
                power_sum_list.append(power_sum)
                j += 1
    print(max(power_sum_list))


if __name__ == "__main__":
    main()


"""
import sys

def main():
    input_list = input().split()
    n = int(input_list[0])
    m = int(input_list[1])
    
    power_dict = {}
    cost_dict = {}
    for i in range(1, n+1):
        power_dict[i] = int(input_list[2*i])
        cost_dict[i] = int(input_list[2*i+1])
    
    sorted_cost_list = sorted(cost_dict.items(), key=lambda pair : pair[1], reverse=True)

    power_sum_list = [0]

    for j in range(n):
        cost_sum = 0
        power_sum = 0
        while cost_sum < m+1 and j < n:
            key = sorted_cost_list[j][0]
            cost = sorted_cost_list[j][1]
            power_sum += power_dict[key]
            cost_sum += cost
            if cost_sum > m:
                break
            else:
                power_sum_list.append(power_sum)
            j += 1
    print(max(power_sum_list))
if __name__ == '__main__':
    main()

"""