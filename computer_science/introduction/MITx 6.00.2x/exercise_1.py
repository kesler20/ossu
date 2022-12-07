import itertools
from typing import List, Tuple
from dataclasses import dataclass


@dataclass
class Item:
    """Vector of size 2 containing <Weight,Value>"""
    _name: str
    _weight: int
    _value: int

    @property
    def value(self) -> int:
        return self._value

    @property
    def weight(self) -> int:
        return self._weight


def generate_power_set(n: int) -> List[List[int]]:
    """Returns all the possible configurations of V assuming that the
    indices of the items in I mirror the index of the items in V"""
    init = []
    for i in range(n):
        init.append(i)
    combos = []
    for L in range(len(init) + 1):
        for subset in itertools.combinations(init, L):
            combos.append(list(subset))
    power_set: List[List[int]] = []
    for index, combo in enumerate(combos):
        power_set.append([])
        for i in range(len(init)):
            if i in combo:
                power_set[index].append(1)
            else:
                power_set[index].append(0)
    return power_set


def calculate_values_and_weights(I: List[Item]) -> List[Tuple[List[int], int, int]]:
    n = len(I)
    power_set = generate_power_set(n)
    values_and_weights = []
    for set in power_set:
        value_for_set = []
        weights_for_set = []
        for i, taken in enumerate(set):
            value_for_set.append(I[i].value*taken)
            weights_for_set.append(I[i].weight*taken)
        values_and_weights.append(
            (set, sum(value_for_set), sum(weights_for_set)))
    return values_and_weights


def apply_constraint(w: int, weighted_power_set: List[Tuple[List[int], int, int]]) -> List[Tuple[List[int], int, int]]:
    filtered_power_set = list(filter(lambda set: set[1] < w, weighted_power_set))
    print(filtered_power_set)
    return filtered_power_set

def calculate_max_value(filtered_power_set: List[Tuple[List[int],int,int]]):
  max_val = 0
  for set in filtered_power_set:
    if set[1] > max_val:
      max_val = set[1]
  return list(filter(lambda set: set[1] == max_val, filtered_power_set))


# Implementation of the Brute force solution for the Knapsack Problem
I: List[Item] = [Item("Dirt", 4, 0), Item("Computer", 10, 30), Item(
    "Fork", 5, 1), Item("Problem Set", 0, -10)]  # vector containing all the items

print(calculate_max_value(apply_constraint(14, calculate_values_and_weights(I))))
