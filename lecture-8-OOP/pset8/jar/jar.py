# Implement a Python program where we create a class Jar

class Jar:
    # initialize __init__
    def __init__(self, capacity=12, size=0):
        # error check: if capacity is a negative we'll raise a ValueError
        if capacity < 0:
            raise ValueError("Not a valid integer")
        self._capacity = capacity
        self._size = size

    # initialize __str__
    def __str__(self):
        n = "🍪"
        return f"{self.size * n}"

    # custom method
    def deposit(self, n):
        # check: if capacity is at MAX we raise ValueError
        if n > self.capacity or n + self.size > self.capacity:
            raise ValueError("Too many cookies")
        else:
            self._size += n

    # custom method
    def withdraw(self, n):
        # check: if removing too many cookies from jar we raise ValueError
        if n > self.size:
            raise ValueError("Too few cookies")
        else:
            self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

def main():
    # instantiate a cookie_jar with Jar class
    cookie_jar = Jar()
    cookie_jar.deposit(5)
    cookie_jar.withdraw(3)
    print(cookie_jar.capacity) # 12
    print(cookie_jar.size) # 2
    print(cookie_jar) # 🍪🍪

if __name__ == "__main__":
    main()