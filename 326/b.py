def main(n:int):
    
    for i in range(n, 1000):
        num_str = str(i)
        handreds = int(num_str[0])
        tens = int(num_str[1])
        ones = int(num_str[2])
        if handreds*tens == ones:
            print(i)
            break

if __name__ == "__main__":
    n = int(input())
    main(n=n)