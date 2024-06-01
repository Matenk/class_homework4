class Buiding:
    TOTAL = 0
    def __init__(self, value):
        Buiding.TOTAL += 1
        print(Buiding.TOTAL)
        print(list_build)
    def __str__(self):
        return f'Объект {Buiding.TOTAL}'


list_build = []
for i in range(40):
    list_build.append(Buiding(i))




