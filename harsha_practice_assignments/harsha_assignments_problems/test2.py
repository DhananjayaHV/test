def Fun(n):
    if n % 2 == 0:
        if 2 <= n <= 5:
            print("Not wired")
        elif 6 <= n <= 20:
            print("wired")
        elif n > 20:
            print("Not wired")

    else:
        print("Weird")


if __name__ == '__main__':
    n = int(input().strip())
    Fun(n)
