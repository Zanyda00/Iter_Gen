class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.x = 0
        self.y = 0

    def __iter__(self):
        self.value = self.list_of_list[self.y][self.x]
        return self

    def __next__(self):
        while self.y < len(self.list_of_list):
            self.value = self.list_of_list[self.y][self.x]
            if self.x < len(self.list_of_list[self.y]) - 1:
                self.x += 1
            else:
                self.y += 1
                self.x = 0
            return self.value
        else:
            raise StopIteration



def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()