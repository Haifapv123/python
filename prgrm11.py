names=input("enter first names seperated by space:").split()
count=0
for name in names:
 count+=name.lower().count('a')
print("number of occurence of 'a':",count)
