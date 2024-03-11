class HashMap:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]

    def _hash(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        index = self._hash(key)
        bucket = self.buckets[index]
        for i, (existing_key, existing_value) in enumerate(bucket):
            if existing_key == key:
                # Update existing key's value
                bucket[i] = (key, value)
                return
        # Key not found, add new key-value pair
        bucket.append((key, value))
        self.size += 1

    def get(self, key, default=None):
        index = self._hash(key)
        bucket = self.buckets[index]
        for existing_key, value in bucket:
            if existing_key == key:
                return value
        return default

    def delete(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]
        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                del bucket[i]
                self.size -= 1
                return
        raise KeyError(f"Key '{key}' not found")

    def __len__(self):
        return self.size

    def __repr__(self):
        items = ', '.join([f"{key}: {value}" for bucket in self.buckets for key, value in bucket])
        return "{" + items + "}"

# Example usage:
if __name__ == "__main__":
    my_map = HashMap()
    my_map.insert("apple", 5)
    my_map.insert("banana", 10)
    my_map.insert("cherry", 15)

    print(my_map)  # Output: {apple: 5, banana: 10, cherry: 15}

    print(my_map.get("banana"))  # Output: 10

    my_map.delete("banana")
    print(my_map)  # Output: {apple: 5, cherry: 15}
