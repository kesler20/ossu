from typing import List


class Food(object):

    def __init__(self, n, v, w) -> None:
        self.name = n
        self.value = v
        self.calories = w

    def getValue(self):
        return self.value

    def getCost(self):
        return self.calories

    def density(self):
        return self.getValue()/self.getCost()

    def __str__(self):
        return f"{self.name} : < {self.value}, {self.calories} >"


def buildMenu(names, values, calories):
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))

    return menu


def greedy(items, max_cost, key_function):
    """Implementation of a flexible greedy algorithm
    (independent by the definition of best)"""
    # sort the items from best to worst according to the key_function (our definition of best)
    items_copy: List[Food] = sorted(items, key=key_function, reverse=True)
    result = []
    total_value, total_cost = 0, 0
    # ass items to the result until max_cost is reached
    for i in range(len(items_copy)):
        if (total_cost + items_copy[i].getCost()) <= max_cost:
            result.append(items_copy[i])
            total_cost += items_copy[i].getCost()
            total_value += items_copy[i].getValue()

    return (result, total_value)


def testGreedy(items, constraint, key_function):
    taken, val = greedy(items, constraint, key_function)
    print(f"Total value of items takes = {val}")
    for item in taken:
        print(item)


def testGreedys(foods, max_units):
    print("Use greedy by value to allocate", max_units, 'calories')
    testGreedy(foods, max_units, Food.getValue)
    print("\nUse greedy by cost to allocate", max_units, 'calories')
    testGreedy(foods, max_units, lambda x: 1/Food.getCost(x))
    print("\nUse greedy by density to allocate", max_units, 'calories')
    testGreedy(foods, max_units, Food.density)

if __name__ == "__main__":
  names = ['wine', 'beer', 'pizza', 'burger',
          'fries', 'cola', 'apple', 'donut', 'cake']
  values = [89, 90, 95, 100, 90, 79, 50, 10]
  calories = [123, 154, 258, 354, 365, 150, 95, 195]
  foods = buildMenu(names, values, calories)
  testGreedys(foods, 800)
