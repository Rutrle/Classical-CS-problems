class TowerStack:
    def __init__(self):
        self._container = []
    def push(self, item):
        self._container.append(item)
    def pop(self):
        return self._container.pop()

    def __repr__(self) -> str:
        return 'bottom ->' + str(self._container)
        

num_discs = 20
tower_a = TowerStack()
tower_b = TowerStack()
tower_c = TowerStack()

for i in range(1, num_discs + 1):
    tower_a.push(i)
print(tower_a)

def hanoi(begin, end, temp, n): 
    if n == 1:
        end.push(begin.pop())
    else:
        hanoi(begin, temp, end, n - 1)
        hanoi(begin, end, temp, 1)
        hanoi(temp, end, begin, n - 1)

hanoi(tower_a, tower_c, tower_b, num_discs)
print(tower_a)
print(tower_b)
print(tower_c)       