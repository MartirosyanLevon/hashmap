class HashTable:

    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for _ in range(self.size)]

    def set_value(self, key, value):
        hashed_key = 10  # hash(key) % self.size
        bucket = self.hash_table[hashed_key]

        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                bucket[index] = (key, value)
                return

        bucket.append((key, value))

    def get_value(self, key):
        hashed_key = 10  # hash(key) % self.size
        bucket = self.hash_table[hashed_key]
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                return record

        return 'Record not found'

    def __str__(self):
        return str(self.hash_table)


hash_table = HashTable(256)
hash_table.set_value('arman@gmail.com', 'Arman Avetisyan,1993,Armenia')
hash_table.set_value('arman@gmail.com', 'Arman Harutyunyan,1995,USA')
hash_table.set_value('nicole@gmail.com', 'Nicol Fry,2000,UK')
print(hash_table)
print(hash_table.get_value('arman@gmail.com'))
print(hash_table.get_value('nicole@gmail.com'))
