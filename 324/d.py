import itertools
import math

def main(n:int, s:str):
    all_s = list(itertools.permutations(s))
    all_num = set([int("".join(s)) for s in all_s])
    count = 0
    for num in all_num:
        if is_square_num(n=num):
            count += 1
            
    print(count)

def is_square_num(n:int):
    sqrt_n = math.sqrt(n)
    if sqrt_n.is_integer():
        return True
    else:
        return False
    
if __name__=="__main__":
    n = int(input())
    s = str(input())
    main(n=n, s=s)

"""
メモ:n<=13だから
最高で
9999999999999

このとき、最高の平方数は
3162277
"""