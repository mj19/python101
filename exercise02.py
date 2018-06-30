#6 key-values as parameters
def demo(**args_v):
    for k,v in args_v.items():
        print(k,v)

demo(name="mjmj",age=18)

#7 range(100), python3 return iterator vs python2 return list
print(range(1,10))
print(list(range(1,10)))

#8 data type: int, book, str, list, tuple, dict
list1 = [1,2,3,4]
tuple = (1,2,3,4)
dict = {"num":"1", "name":"mj"}
print(list1)
print(tuple)
print(dict)

#9 class __init__
class Bike:
    def __init__(self, newColor):
        self.color = newColor

    def move(self):
        print("move on ..")

BM = Bike("Blue")
print("Color is: %s"%BM.color)

#10 map() 内置的高阶函数，
# 接收一个函数 f 和一个 list，并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的 list 并返回
l1 = [1,2,3,4]
def f(x):
    return x**2
ma = map(f,l1)
print(ma)
print(list(ma))
