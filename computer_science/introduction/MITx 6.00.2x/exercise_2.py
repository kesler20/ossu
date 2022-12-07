from typing import List


class Item(object):

    def __init__(self, n, v, w) -> None:
        self.name = n
        self.value = v
        self.weight = w

    def getValue(self):
        return self.value

    def getWeight(self):
        return self.weight

    def density(self):
        return self.getValue()/self.getWeight()

    def __str__(self):
        return f"{self.name} : < {self.value}, {self.weight} >"


def buildCollection(names, values, weight):
    menu = []
    for i in range(len(values)):
        menu.append(Item(names[i], values[i], weight[i]))

    return menu


def greedy(items, max_weight, key_function):
    """Implementation of a flexible greedy algorithm
    (independent by the definition of best)"""
    # sort the items from best to worst according to the key_function (our definition of best)
    items_copy: List[Item] = sorted(items, key=key_function, reverse=True)
    result = []
    total_value, total_weight = 0, 0
    # ass items to the result until max_weight is reached
    for i in range(len(items_copy)):
        if (total_weight + items_copy[i].getWeight()) <= max_weight:
            result.append(items_copy[i])
            total_weight += items_copy[i].getWeight()
            total_value += items_copy[i].getValue()

    return (result, total_value)


def testGreedy(items, constraint, key_function):
    taken, val = greedy(items, constraint, key_function)
    print(f"Total value of items takes = {val}")
    for item in taken:
        print(item)


def testGreedys(foods, max_units):
    print("Use greedy by value to allocate", max_units, 'Kg')
    testGreedy(foods, max_units, Item.getValue)
    print("\nUse greedy by weight to allocate", max_units, 'Kg')
    testGreedy(foods, max_units, lambda x: 1/Item.getWeight(x))
    print("\nUse greedy by density to allocate", max_units, 'Kg')
    testGreedy(foods, max_units, Item.density)

if __name__ == "__main__":
  names = ['clock', 'picture', 'radio', 'vase',
          'book', 'computer']
  values = [175, 90, 20, 50, 10, 200]
  weight = [10, 9, 4, 2, 1, 20]
  foods = buildCollection(names, values, weight)
  testGreedys(foods, 20)
