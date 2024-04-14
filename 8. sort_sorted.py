from operator import itemgetter

my_list = ["abcd", "efg", "hi", "j"]
my_list = sorted(my_list, key=len)

print(my_list)
print()


data = [("John", 28, "A"), ("Alice", 23, "B"), ("Bob", 32, "C")]
print("Sort norm:", sorted(data))
print("Sort by name - index 0:", sorted(data, key=itemgetter(0)))
print("Sort by age - index 1:", sorted(data, key=itemgetter(1)))
print("Sort by letter - index 2:", sorted(data, key=itemgetter(2)))
