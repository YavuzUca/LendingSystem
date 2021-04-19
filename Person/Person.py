class Person:
    def __init__(self, id, gender, nameSet, firstName, surname, permissionLevel = 1):
        self._id = id
        self._gender = gender
        self._nameSet = nameSet
        self._firstName = firstName
        self._surname = surname
        self._permissionLevel = permissionLevel