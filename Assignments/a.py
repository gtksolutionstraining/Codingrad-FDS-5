class A:
    def __init__(self) -> None:
        self.a = "a"
        self._b = "b"
    def get_a(self):
        return self.a
    
a = A()
print(f"Public Property:{a.a}")
print(f"Protected Property:{a._b}")