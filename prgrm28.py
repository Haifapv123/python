start = int(input("Enter start: "))
end = int(input("Enter end: "))

for n in range(start, end + 1):
    if 1000 <= n <= 9999:
        if all(int(d) % 2 == 0 for d in str(n)):
            if int(n ** 0.5) ** 2 == n:
                print(n)
