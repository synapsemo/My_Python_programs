# class A:
#     def __init__(self, a):
#         self.a = a
#         print(self.a)
# class B:
#     def __init__(self, b):
#         self.b = b
#         print(self.b)

#     def test(self):
#         print("demoe")

# class C(A, B):
#     def __init__(self, a , b):
#         super().__init__(a=a)

#     def test(self):
#         print("demo")

# i = C(234,43)

# print(i.mro())



class Demo:
    # def __new__(self, *args, **kwargs):
    #     print(*args)
    #     print(**kwargs)
    #     return self

    def __init__(self):
        print("34")
        pass

    def __call__(self, *args , **kwds):
        print("234")
        pass

    def __str__(self) -> str:
        return "et"


    def test(self):
        print("yes")


s = Demo()
print(s.mro())
print(s.test())
