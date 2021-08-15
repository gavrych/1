class House:
    flat_count = 0
    room_count = 0

    def __str__(self):
        return 'house'

    def __init__(self, n):
        self.number = n[0]
        self.year = n[1]
        self._material = n[2]
        self._num_floor = n[3]
        self._price = n[4]
        House.flat_count += 1
        print(House.flat_count, self)


#house = [['house1', 2021, 'brick', 9, 100000], ['house2', 2015, 'wood', 3, 70000], ['house3', 2016, 'panel', 20, 50000]]
h = {'house1': [1, 2021, 'brick', 9, 100000], 'house2': [2, 2015, 'wood', 3, 70000], 'house3': [3, 2016, 'panel', 20, 50000]}
for key, val in h.items():
    globals()[key] = House(val)
a = House([3,2000,'shlack',2,30000])
print(house2._price)
print(House.__dict__)
print(house2.__dict__)
print(house1._price/a._num_floor)
