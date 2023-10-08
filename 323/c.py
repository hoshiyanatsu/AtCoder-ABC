def main(n:int, m:int, a_list:list, s_list:list):
    score_dict = {}
    a_dict = {}
    for i in range(m):
        a_dict[i+1] = a_list[i]
    for i in range(n):
        i_score = i+1
        for j in range(m):
            if s_list[i][j] == "o":
                i_score += a_list[j]
        
        score_dict[i+1] = i_score
    max_score = max(score_dict.values())
    a_sorted_list = sorted(a_dict.items(), key=lambda x:x[1], reverse=True)
    
    for i in range(n):
        will_solve_count = 0
        if score_dict[i+1] != max_score:        
            will_solve_score = 0
            for j, score in a_sorted_list:
                if s_list[i][j-1]=="x":
                    will_solve_score += score
                    will_solve_count += 1
                if score_dict[i+1]+will_solve_score > max_score:
                    break

        print(will_solve_count)


if __name__ == "__main__":
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    s_list = [input() for _ in range(n)]
    main(n=n, m=m, a_list=a_list, s_list=s_list)