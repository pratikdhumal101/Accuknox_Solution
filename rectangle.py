class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __iter__(self):
        yield 'length', self.length
        yield 'width', self.width

# Take input from the user for length and width
length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))

# Create an instance of Rectangle with user input
rectangle = Rectangle(length, width)

# Iterate over the rectangle and print its dimensions
for dimension, value in rectangle:
    print(f'{dimension}: {value}')
