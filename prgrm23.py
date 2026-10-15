d = {}

n = int(input("Enter number of items: "))

for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    d[key] = value

ascending = dict(sorted(d.items(), key=lambda item: item[1]))
descending = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

print("Ascending order:", ascending)
print("Descending order:", descending)
