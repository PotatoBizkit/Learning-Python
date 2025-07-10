class DemonHunter:

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and value:
            self._name = value
        else:
            raise ValueError("Invalid name")
    
me = DemonHunter()
me.name = "Cheeze Nutz"
print(me.name)