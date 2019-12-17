l1 = [1,2,3,4,5]
l2 = [22,21,34,5,44,23]
# stops @ short list as it looks for pair

for a,b in zip(l1,l2):
    print(a)
    print(b)

print("*"*30)

for a, b in zip(l1, l2):
    if a>b:
        print(a)
    else:
        print(b)