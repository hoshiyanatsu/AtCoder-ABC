def main(n: int, m: int, a_list: list):
    ans = 0
    r = 0
    for i in range(n):
        while a_list[r] < a_list[i]+m:
            r += 1
        ans = max(ans, r-i)
    print(ans)

if __name__ == '__main__':
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    a_list.sort()
    a_list.append(10**10+1)
    main(n=n, m=m, a_list=a_list)