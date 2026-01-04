class Item:
    def __init__(self, name, size, point):
        self.name = name
        self.size = size
        self.point = point

items = [Item("r", 3, 25), Item("p", 2, 15), Item("a", 2, 15),
        Item("m", 2, 20), Item("i", 1, 5), Item("k", 1, 15),
        Item("x", 3, 20), Item("t", 1, 25), Item("f", 1, 15),
        Item("d", 1, 10), Item("s", 2, 20), Item("c", 2, 20)]

items = sorted(items, key=lambda x: x.point / x.size, reverse=True)

# вариант 1
# болезней нет
knapsack_size = 2 * 4-1
points = 15

knapsack = []
answer = []
weight = 0

delanswer = []

while knapsack_size > weight:
    if (items[0].size + weight) <= knapsack_size:
        knapsack.append(items[0])
        weight += items[0].size
        del items[0]
    elif (knapsack_size - weight) < items[0].size:
        delanswer.append(items[0].point)
        del items[0]
    else:
        break

for i in knapsack:
    points += i.point
    for a in range(i.size):
        answer.append(i.name)

for i in items:
    points -= i.point
points -= sum(delanswer)

print(f'Очки выживания - {points}\nРюкзак:\n{answer[:4]}\n{answer[4:]}')