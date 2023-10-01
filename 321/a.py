n_str = str(input())
is_321 = True
for i in range(len(n_str)-1):
    if int(n_str[i]) <= int(n_str[i+1]):
        print("No")
        is_321 = False
        break

if is_321:
    print("Yes")