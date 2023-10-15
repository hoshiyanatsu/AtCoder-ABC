def main(n:int, t:str, s_list:list):
    ans_list = []
    for i, s in enumerate(s_list):
        if len(t)==len(s):
            if is_same_str(t=t, t_dash=s):
                ans_list.append(i+1)
            elif is_replace_str(t=t, t_dash=s):
                ans_list.append(i+1)
        elif len(t)+1==len(s):
            if is_insert_str(t=t, t_dash=s):
                ans_list.append(i+1)
        elif len(t)-1==len(s):
            if is_delete_str(t=t, t_dash=s):
                ans_list.append(i+1)

    print(len(ans_list))
    print(*ans_list)

def is_same_str(t:str, t_dash:str):
    if t==t_dash:
        return True
    
    return False

def is_insert_str(t:str, t_dash:str):
    same = True
    for i in range(len(t_dash)):
        if same:
            if i==len(t)-1:
                if t[i] == t_dash[i]:
                    return True
            if t[i] != t_dash[i]:
                same = False
        else:
            if t[i-1] != t_dash[i]:
                return False
    return True

def is_delete_str(t:str, t_dash:str):
    same = True
    for i in range(len(t_dash)):
        if same:
            if t[i] != t_dash[i]:
                if t[i+1] != t_dash[i]:
                    return False
                same = False
        else:
            if t[i+1] != t_dash[i]:
                return False
    return True
            
def is_replace_str(t:str, t_dash:str):
    same = True
    for i in range(len(t)):
        if same:
            if t[i] != t_dash[i]:
                same = False
        else:
            if t[i] != t_dash[i]:
                return False
    return True

if __name__=="__main__":
    n, t = map(str, input().split())
    n = int(n)
    s_list = [input() for _ in range(n)]
    main(n=n, t=t, s_list=s_list)