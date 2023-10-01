def main(n:int, m:int, s_list:list, t_list:list):
    # S が T の接頭辞であり、かつ接尾辞でもある場合は 0 を、
    # S が T の接頭辞であるが、接尾辞でない場合は 1 を、
    if t_list[:n]==s_list:
        if t_list[m-n:]==s_list:
            return 0
        else:
            return 1
    elif t_list[m-n:]==s_list:
        return 2
    else:
        return 3
    
    # S が T の接尾辞であるが、接頭辞でない場合は 2 を、
    # S が T の接頭辞でも接尾辞でもない場合は 3 を出力してください。

if __name__=="__main__":
    n, m = map(int, input().split())
    s_list = list(input())
    t_list = list(input())
    ans = main(n=n, m=m, s_list=s_list, t_list=t_list)
    print(ans)
