stringOfNames = "Bob, Nancy, Joe"
listOfNames = ["Jack, Robert, Lena"]
listOfIds = ["24, 32, 1, 232, 9421, 42"]

class CustomObject:
    def __init__(self):
        self.name = []
        self.id = ""
        self.disabled = []
        self.projectid = []

    def addNameString(self, name):
        self.name.append(name)

    def addNameList(self, name):
        self.name += name

    def addID(self, id):
        self.id += id

    def __str__(self): # __str__ is called when instance of object is printed
        return (str(self.name))


u = CustomObject()

u.addNameString(stringOfNames)
u.addNameList(listOfNames)

print(u)

for id in listOfIds:
    u.addID(id)

print(u.id)

# print(dir(u))  # Returns object attributes
