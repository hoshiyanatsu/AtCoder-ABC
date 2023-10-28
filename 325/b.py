def main(n:int, w_x_pairs:list):
    jikoku_lists = [[(i+j)%24 for i in range(9)] for j in range(24)]
    max_numbers_staff = 0
    for jikoku_list in jikoku_lists:
        numbers_staff = 0
        for w, x in w_x_pairs:
            if x in jikoku_list:
                numbers_staff += w
        if numbers_staff > max_numbers_staff:
            max_numbers_staff = numbers_staff
    print(max_numbers_staff)

if __name__=="__main__":
    n = int(input())
    w_x_pairs = [list(map(int, input().split())) for _ in range(n)]
    main(n=n, w_x_pairs=w_x_pairs)