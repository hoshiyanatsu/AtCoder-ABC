import math
def main(k:int):
    a_digit_list = [str(i) for i in range(1, 10)]
    double_digit_list = []
    for d in a_digit_list:
        d_int = int(d)
        
    count = 0
    for n_str in range(number_list):
        if is_123(n_str=n_str):
            count += 1
        if count>=k:
            break
    print(count)

def is_123(n_str:str):
    ans = True
    for i in range(len(n_str)-1):
        if int(n_str[i]) <= int(n_str[i+1]):
            ans = False
            return ans
    return ans
    
if __name__ == "__main__":
    k = int(input())
    main(k=k)