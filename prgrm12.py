list1 = list(map(int, input("Enter the first list: ").split()))
list2 = list(map(int, input("Enter the second list: ").split()))

if len(list1) == len(list2):
    print("Lists are of same length")
else:
    print("Lists are not of same length")

if sum(list1) == sum(list2):
    print("Lists have the same sum")
else:
    print("Lists do not have the same sum")

if set(list1).intersection(set(list2)):
    print("Both lists contain common values")
else:
    print("No common values")
list1=list(map(input("enter the first list:").split()))
list2=list(map(input("enter the second list:").split()))
if len(list1)==len(list2):
 print("list are of same length")
else:
 print("list are not  of same length")
 
if sum(list1)==sum(lis2):
 print("list are of same value")
else:
 print("list are ot same value")
if set(list1).intersection(set(list2)):
 print("both list  contain common value")
else:
 print("no common value")
