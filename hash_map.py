class HashMap:
    def __init__(self, capacity=500):
        self.capacity = capacity
        self.size = 0
        self.keys = []
        self.values = [[] for _ in range(capacity)]

    def _increase_size(self):
        prev_values = [value for value in self.values if value != []]

        self.capacity *= 2
        self.size = 0
        self.keys.clear()
        self.values = [[] for _ in range(self.capacity)]

        for bucket in prev_values:
            for item in bucket:
                self.set(item[0], item[1])

    def _handle_collision(self, index, key, value):
        bucket = self.values[index]
        existing_key = False

        for counter, item in enumerate(bucket):
            if item[0] == key:
                existing_key = True
                break

        if existing_key:
            bucket[counter] = (key, value)
        else:
            bucket.append((key, value))
            self.size += 1

    def hash_function(self, key):
        return hash(key) % self.capacity

    def set(self, key, value):
        index = self.hash_function(key)

        self.keys.append(key)

        if not self.values[index]:
            self.values[index] = [(key, value)]
            self.size += 1
        else:
            self._handle_collision(index, key, value)

        if self.size >= self.capacity * 0.75:
            self._increase_size()

    def get(self, key):
        index = self.hash_function(key)
        bucket = self.values[index]
        found_item = False

        for counter, item in enumerate(bucket):
            if item[0] == key:
                return item[1]

        raise KeyError(key)

    def delete(self, key):
        index = self.hash_function(key)
        bucket = self.values[index]
        existing_key = False

        for counter, item in enumerate(bucket):
            if item[0] == key:
                deleted = bucket[counter]

                del bucket[counter]
                self.keys.remove(key)
                self.size -= 1

                return deleted

        raise KeyError(key)
