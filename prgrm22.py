numbers = list(map(int, input("Enter integers separated by space: ").split()))
positive = (n for n in numbers if n > 0)
print("Positive numbers:", list(positive))


n = int(input("Enter n: "))
square = [i * i for i in range(1, n + 1)]
print("Squares:", square)



word = input("Enter a word: ")
vowels = [ch for ch in word if ch.lower() in "aeiou"]
print("Vowels:", vowels)


words = input("Enter a word: ")
values = [ord(ch) for ch in words]
print("Original values:", values)
