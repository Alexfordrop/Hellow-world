class Collection:
    def __init__(self, list):
        self.list = list

    def __len__(self):
        return len(self.list)

collection = Collection([1, 2, 3, 9])
print(len(collection))