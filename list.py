l1 = ["Bangalore","bangalore","Hyd","Lcw","Delhi","bangalore","bangalore"]
print(l1.count("Bangalore"))
l1.append("Mumbai")
print(l1)
l1.pop()
print(l1)
l1.pop(1)
print(l1)
l1.remove("Hyd")
print(l1)
l1.insert(0,"J&K")
print(l1)
l1.sort()
print(l1)

print('*'*100)

l2 = [1,2,3,4,6]
l2.sort()
print(l2)
print(l2[3]+1)
print("Total values in the list ",len(l2))
print('*'*100)

l1 = ["Bangalore","bangalore","Hyd","Lcw","Delhi","bangalore","Chennai"]

x =  l1.index("bangalore")
print("Index",x)

l1 = "Arvind"
print(l1[::-1])

print("*"*100)


cars = ["MG","kia","honda","BMW","Maruthi"]
v1 = cars.index("honda")
print(cars[v1:])

print(cars)
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

print("#"*100)
bike=["hero"]
cars.extend(bike)
print(cars)

print("#"*100)

empty = []
empty.append("ARVIND")
print(empty)
print("#"*100)

c1 = ["mg","4000","white","Door"]
c2 = ["model","cc","colour","3"]
for c in zip(c1,c2):
    print(c)
    print(type(c))

print("*"*100)


# empty Set
car = set()
car.add("Arvind")
car.add("Azar")
car.add("Azar")
car.add("Zoom")
car.add("Kar")
car.update("Zoom")
print(car)

print("*"*100)

list = ["Arvind","Azar","Teju","Rashmi","Harish","Arvind","Arvind"]
list2 = [2,3,4,4]

list.extend(list2)
print(list)

print("*"*100)
# Built in methods to help manipulating strings
car = ['bmw', 'honda', 'audi']
length =len(car)
print("Lenght of the list "+str(length))
car.append("kia")
print(car)
car.insert(2,"Jeep")
print(car)
x = car.index("audi")
print("Car index is "+str(x))
# pop method gives the return value
y =  car.pop()
print("Delete the last car "+ str(y))
car.remove("Jeep")
print("Final list "+ str(car))
# First index is inclusive and last is exclusive
sliceing =  car[0:2]
print(sliceing)
# Stating from 1st index
a=car[1:]
print(a)
car.sort()
print(car)

list = [1,2,3,4]
list.extend(car)
print(list)

