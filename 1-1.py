class StringVar:

    def __init__(self, str):
        self.str = str


    def set(self, str):
        self.str = str


    def get(self):
        return self.str


a = StringVar('name')
a.set('age')
print(a.get())
