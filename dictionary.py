#Dictionary methods
car = {"make":"bmw", "Model": '550i', 'year': 2019}
cars = {'bmw': {'model':'550i','year':2016}, 'Benz': {'model':'c-Class','year':2019},}

print(car.keys())
print(cars.keys())

print(car.values())
print(cars.values())

print("Items in the dict "+str(cars.items()))
car_copy =  car.copy()
print(car_copy)
print(car.pop('Model'))
print(car)
print(car.clear())


print("*"*100)

car = {"make":"bmw", "Model": '550i', 'year': 2019}

print(car)

print(car['make'])

print("*"*100)

# Empty dictionary
d= {}
d['one']=1
d['two']=2
print(d)
sum_num = d['two']+3
print(sum_num)
print(d)
# Adding value to the dic on the fly
d['two'] = d['two']+3
print(d)

print("*"*100)

# Nested Dictonery
val = {"Automation QA":{"ISTQ":"Yes","AutoTool":"selenium","DB tool":"mysql"},"QA":{"Manual","MYSQL","ServerSide"}}
print(val['Automation QA']['ISTQ'])
print(val['Automation QA'].values())
print(val['QA'])

print("*"*100)

car = {'bmw': {'model':'550i','year':2016}, 'Benz': {'model':'c-Class','year':2019},'audi':{"model":"Q7",'year':"2019"}}
print(car)
bmw_yr = car['bmw']['year']
print(bmw_yr)
print(car['Benz']['model'])
print(car.values())
print(car.keys())
