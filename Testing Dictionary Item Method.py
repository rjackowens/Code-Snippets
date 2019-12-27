d = {'H': 1.008, 'He': 4.003, 'Li': 6.94}

for elements, weights in d.items():
    print(elements, weights)

listOfElements = list(elements for elements, weight in d.items())
listOfWeights = list(weight for elements, weight in d.items())

print(listOfElements, listOfWeights)
#print(listOfWeights)
