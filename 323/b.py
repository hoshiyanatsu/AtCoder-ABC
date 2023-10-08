def main(n:int, s_list:list):
    count_win_dict = {}
    for i in range(len(s_list)):
        count_win = 0
        for j in range(len(s_list[i])):
            if s_list[i][j] == "o":
                count_win += 1
        count_win_dict[i+1] = count_win
    
    sorted_count_win_dict = sorted(count_win_dict.items(), key=lambda x:x[1], reverse=True)
    for i in range(len(sorted_count_win_dict)):
        print(sorted_count_win_dict[i][0], end=" ")
    print()

if __name__ == "__main__":
    n = int(input())
    s_list = [str(input()) for _ in range(n)]
    main(n=n, s_list=s_list)