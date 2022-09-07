import json

class Model:

    def __init__(self, dict):
        self.dict = dict

    def set(self, dict):
        self.dict = dict

    def get(self):
        return self.dict

    def save(self):
        dictionary = Model.__dict__
        with open('mod.json', 'w') as f:
            return json.dump(dictionary, f)

d = Model('5')
d.save()
print(d.__dict__)


///Это задание не смогла выполнить целиком. Класс и три метода работают. Все, что связано с JSON, не работает.///