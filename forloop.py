d = {"make":"bmw", "Model": '550i', 'year': 2019}
print(d.items())
for k in d:
    print(k)


print("*"*30)
for m in d:
    print(m +" "+str(d[m]))
  #  print("#" * 30)

   # print(m + " " + str(d.values()))

print("*"*30)

l = [1,2,4]
for x in l:
    print(x*5)

print("#" * 30)

for k,v in d.items():
    print(k)
    print(v)


"""
 We can use the loops to iterate on the Strings, list, tuples, set, Dictionary

"""
print("#"*100)
myString= 'abcabcaaa'

for c in myString:
    if c=='a':
        print("A", end='')
    else:
        print(c, end='')

print(c, end='')

cars = ['bmw', 'honda', 'audi']

for car in cars:
    if car == 'bmw':
        print("BMW", end='')
    else:
        print(car,end='')
