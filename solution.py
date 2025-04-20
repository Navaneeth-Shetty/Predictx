def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        if n < 4:
            print("NO")
        elif n == 5 or n == 7:
            print("NO")
        else:
            print("YES")

if __name__ == "__main__":
    solve() 