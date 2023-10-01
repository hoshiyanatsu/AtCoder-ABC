def main(n:int, x:int, a_list:list):
    max_score = max(a_list)
    min_score = min(a_list)
    sum_a_list = sum(a_list)
    if sum_a_list-min_score<x:
        ans = -1
    elif sum_a_list-max_score>=x:
        ans = 0
    else:
        ans = x-(sum_a_list-min_score-max_score)
    
    print(ans)

    
if __name__ == "__main__":
    n, x = map(int, input().split())
    a_list = list(map(int, input().split()))
    main(n=n, x=x, a_list=a_list)