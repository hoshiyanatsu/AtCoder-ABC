def main(x:int, y:int):
    if x < y and y-x <3:
        print("Yes")
    elif y < x and x-y <4:
        print("Yes")
    else:
        print("No")
if __name__ == "__main__":
    x, y = map(int, input().split())
    main(x=x, y=y)