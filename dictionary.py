phonebook = {}
phonebook["John"] = 'No number'
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

for name, number in phonebook.items():
    print(f'Phone number of {name} is : {number}')