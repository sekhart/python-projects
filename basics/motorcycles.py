motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
motorcycles.append('honda')
print(motorcycles)
motorcycles.insert(2, 'BMW')
print(motorcycles)
del motorcycles[1]
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

motorcycles.remove('BMW')
print(motorcycles)