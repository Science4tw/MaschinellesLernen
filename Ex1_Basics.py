""" greeting.py"""
def greet(name="Sepp", greeting="Tschou"):
    print(greeting, name)

greet()
greet("Pascal")
greet("Kurt", "Hi")
greet(greeting="Hallo")
greet(name="Marc", greeting="Hallo")

"""printing.py"""
import matplotlib.pyplot as plt

def print_path(x_coords, y_coords):
    plt.plot(x_coords, y_coords)
    plt.show()

x_coords = [0, 1, 2, 3, 4, 5, 6]
y_coords = [2, 3, 2, 6, 6, 5, 2]
print_path(x_coords, y_coords)


"""list_and_dict.py"""
values = [2, 5, -3, 1, 99, 0, 8]
result = values[2:5]
print(result) # [-3, 1, 99]
result = values[:3]
print(result) # [2, 5, -3]
result = values[2:]
print(result) # [-3, 1, 99, 0, 8]
result = values[2::2]
print(result) # [-3, 99, 8]

d = {"one":1, "two":2, "three":3}
d["five"] = 5
d["one"] = 0.5

print(d) # {'one': 0.5, 'two': 2, 'three': 3, 'five': 5}
print(d["two"]) # 2

