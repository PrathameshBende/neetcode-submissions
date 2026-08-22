class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            # Move the key to the end (most recently used)
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update the value and move to end
            self.cache.move_to_end(key)
            self.cache[key] = value
        else:
            # Add new key-value pair
            if len(self.cache) >= self.capacity:
                # Remove the least recently used (first item)
                self.cache.popitem(last=False)
            self.cache[key] = value

