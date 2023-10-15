def main(n:int, a_list:list):
    ans = "Yes"
    for i in range(n-1):
        if a_list[i] != a_list[i+1]:
            ans = "No"
            break
    print(ans)
if __name__=="__main__":
    n = int(input())
    a_list = list(map(int, input().split()))
    main(n=n, a_list=a_list)