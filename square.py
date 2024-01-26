class Square:
    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width

    @property
    def height(self):
        print("Retrieving the height")

        return self.__height

    @height.setter
    def height(self, val):
        self.__height = val


    def getArea(self):
        return int(self.__width) * int(self.__height)

def main():
    a = Square()
    a.height = 4
    print(a.height)

main()
