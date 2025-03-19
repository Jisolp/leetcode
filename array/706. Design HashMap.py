class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.map = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        index = key % self.size
        bucket = self.map[index]
        
        for i,(k,v) in enumerate(bucket):
            if key == k:
                bucket[i] = (key, value)
            return 
        bucket.append((key,value))
    
    def get(self, key: int) -> int:
        index = key % self.size
        bucket = self.map[index]
        
        for i, (k,v) in enumerate(bucket):
            if key == k:
                return v
        return -1

    def remove(self, key: int) -> None:
        index = key % self.size
        bucket = self.map[index]

        for i, (k,v) in enumerate(bucket):
            if key == k:
                bucket.pop(i)
                return 
