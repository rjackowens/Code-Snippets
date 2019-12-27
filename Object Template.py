class customProjectObject:
    def __init__(self, Name, IsDisabled, ProjectGroupId):
        self.Name = Name
        self.IsDisabled = IsDisabled
        self.ProjectGroupId = ProjectGroupId

projectObject = customProjectObject("Test", "False", 42)

print(projectObject.Name)

# Expose all object attributes
print(dir(projectObject))



