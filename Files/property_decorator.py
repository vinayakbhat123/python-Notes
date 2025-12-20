# What is @property?
# @property is a decorator that allows you to access a method like an attribute.
# It helps you control getting, setting, and deleting an attribute without changing how it’s used.
# 📌 It is mainly used for encapsulation.

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    # GETTERS (DO NOT MODIFY STATE)
    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    # SETTERS
    @width.setter
    def width(self, new_width):
        if new_width > self._width:
            self._width = new_width
            print("New width is greater than old width")
        else:
            print("New width is smaller")

    @height.setter
    def height(self, new_height):
        if new_height > self._height:
            self._height = new_height
            print("New height is bigger")
        else:
            print("Old height is bigger")

    # DELETERS
    @width.deleter
    def width(self):
        del self._width
        print("Width deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height deleted")

obj = Rectangle(4, 6)

obj.width = 15     # ✅ updated
obj.height = 1     # ❌ rejected

print(obj.width)   # 15
print(obj.height)  # 6

del obj.width
del obj.height
