my_dictionary = {
    'key_1' : 'car_1',
    'key_2' : 'car_2',
    'key_3' : 'car_3'
}
print(my_dictionary['key_1'])

print('------------------------------')
my_dictionary['key_4'] = 'car_4'
print(my_dictionary)

print('------------------------------')
prices_lookup = { 'apple' : 2.99,
                  'orange' : 1.99,
                    'milk' : 5.80}
print(prices_lookup)
print('')
print("Whats the price of an apple?")
print(f"Prices Lookup: {prices_lookup['apple']}")

d = {'k1' : 1, 'k2' : [0, 1, 2], 'k3' : {'inside_key' : 100, 'shelf' : 'grape'}}
print(d['k3']['shelf'])

print('------------------------------')
e = {'key1' : ['a', 'b', 'c']}

print(e['key1'][2].upper())

print('------------------------------')
d = {'k1' : 1, 'k2' : 200, 'k3' : 300}

print(d.keys())
print(d.items())
print(d.values())
print(d.items())
