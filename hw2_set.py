__author__ = 'Naveen'

class OurSet:
    """OurSet is a class that has one field (a list) and several methods
    that act upon this list. OurSet essentially turns the native list into
    a set, which cannot contain duplicates of items. Additionally, OurSet implements
    two common set operations, union and intersection"""

    """this is the field of "data" that is a list"""
    data = []

    def __init__(self):
        """initializer for the OurSet object"""
        self.data = []

    def add(self, item):
        """adds an item to the set if the item is not already in the set"""
        if not (item in self.data):
            self.data.append(item)
            return True
        else:
            return False

    def add_list(self, list):
        """adds each item in the list to the set if it is not already in the set"""
        a = False
        for item in list:
            if not (item in self.data):
                self.data.append(item)
                a = True

        return a

    def __str__(self):
        """provides a way to print out the set in a pretty format"""
        values = ""
        for x in range(0, (len(self.data) - 1)):
            values = values + str(self.data.__getitem__(x)) + ", "
        values += str(self.data.__getitem__(len(self.data) -1))
        return "<" + values + ">"

    def __len__(self):
        """returns the number of items in the set"""
        return len(self.data)

    def __iter__(self):
        """allows for iteration in the set"""
        for x in self.data: yield x

    def union(self, set2):
        """performs the union operation on two sets, and returns the union of them as a new set"""
        d = OurSet()
        for x in self.data:
            if not (x in set2):
                d.data.append(x)
        return d

    def intersection(self, set2):
        """performs the intersection operation on two sets, and returns the intersection of them as a new set"""
        d = OurSet()
        for x in self.data:
            if (x in set2):
                d.data.append(x)
        return d


if __name__ == "__main__":
    m = OurSet()
    m.add(5)
    m.add(7)
    m.add(5)
    m.add(3)
    m.add(6)
    print(m)

    ko = OurSet()
    ko.add(4)
    ko.add(5)
    ko.add(6)
    ko.add(354)

    print(ko)

    print(ko.intersection(m))
    print(ko.union(m))
