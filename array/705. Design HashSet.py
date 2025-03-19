class MyHashSet:

    def __init__(self):
        self.n = 10000
        self.arr = [[]for _ in range(self.n)]

    def add(self, key: int) -> None:
        index = key % self.n
        if key not in self.arr[index]:
            self.arr[index].append(key)
    def remove(self, key: int) -> None:
        index = key % self.n
        if key in self.arr[index]:
            self.arr[index].remove(key)

    def contains(self, key: int) -> bool:
        index = key %self.n
        return key in self.arr[index]
