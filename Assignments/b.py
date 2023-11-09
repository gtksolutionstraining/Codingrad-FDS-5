import sys
sys.path.append("/Users/gtk/GTK/CodinGrad/Codingrad-FDS-5")
import sys
from Assignments.a import A
class B(A):
    def __init__(self) -> None:
        super().__init__()
        self.b1 = "b1"
    def get_b1(self):
        return self._b
    
a = A()
b = B()
print(f"Public property: {a.a}")
print(f"Proetected Property: {a._b}")
print(f"getting B value: {b.get_b1()}")