class A:
    def __init__(self, a):
        self.a = a
        print(self.a)
class B:
    def __init__(self, b):
        self.b = b
        print(self.b)

    def test(self):
        print("demoe")

class C(A, B):
    def __init__(self, a , b):
        super().__init__(a=a)

    def test(self):
        print("demo")

i = C(234,43)

print(i.mro())