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

# print(C.__mro__)



class Demo:
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)
        # return super().__new__(cls)
       
      

    # def __init__(self):
    #     print("34")
    #     pass


    # it make the the object callable
    # def __call__(self, *args , **kwds):
    #     print("234")
    #     pass

    def __str__(self) -> str:
        return "et"


    def test(self):
        print("yes")


s = Demo()
# print(s())
print(s.test())
# print(s.test())
