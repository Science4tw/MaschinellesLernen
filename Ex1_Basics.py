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

""" Schleifen (Start) """

values = [1,2,3] # Python Liste mit 3 Werten
# Ausgeben der Liste:
for val in values:
    print(val)

# 2 Verschachtelte Schleifen
# 1 Validation of parameter via grid search -> ERHALTE X*Y MODELLLE und bewerte diese jeweils!!
for x in [0.0001, 0.001, 0.01, 0.1]:
    for y in [3, 4, 5, 6, 7, 8, 9, 10]:
        print(x, y)

    # z.B Definiere einen DecisionTree für jede Kombination aus x und y



# Verschachtelte Range Schleifen
for x in range(15, 26, 1): # von 15 bis 25
    for y in range(10, 21, 1): # von 10 bis 20
        print(x, y)

""" Schleifen (Ende)"""

