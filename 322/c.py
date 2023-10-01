def main(n:int, m:int, a_list:list):
    checking_index = 0
    for i in range(n):
        output = a_list[checking_index]-i-1
        print(output)
        if output==0:
            checking_index += 1
    return 0

if __name__=="__main__":
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    main(n=n, m=m, a_list=a_list)