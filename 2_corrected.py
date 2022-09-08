import json

class Model:

    def __init__(self, dict):
        self.dict = dict

    def set(self, dict):
        self.dict = dict

    def get(self):
        return self.dict

    def save(self):
        dictionary = self.__dict__
        with open('mod.json', 'w') as f:
            json.dump(dictionary, f)


d = Model('89')
d.save()
print(d.__dict__)

#В таком виде все работает. Но в JSON заисывается только один элемент. Если создать еще один объект, то он не сохраняется в JSON.