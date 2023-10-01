N = int(input())
S = input()
if "ABC" not in S:
    print(-1)
else:
    ans = 0
    for i in range(len(S)-2):
        if S[i]=="A" and S[i+1]=="B" and S[i+2]=="C":
            print(i+1)
            break