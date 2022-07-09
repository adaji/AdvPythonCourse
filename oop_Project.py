class human:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


names = ["mohsen", "hosein", "maziyar", "akbar", "nima", "mehdi", "farhad", "mohamad", "khashayar", "milad",
         "mostafa", "amin", "said", "pooya", "pooria", "reza", "ali", "behzad", "soheil", "shahrooz", "saman", "behrooz"]

objects = list()
for name in names:
    objects.append(human(name))

for item in objects:
    print("name: %s" % item)


class footballist(human):
    pass
