#1 sum 1 -- 100
print(sum(range(0,101)))


#2 global 修改全局变量
a = 5
def fn():
    global a
    a = 4

fn()
print(a)

#3 dictionary update and del
dic = {"name":"mj","age":18}
del dic["name"]
#print(dic)
dic2 = {"name":"xn","age":"19"}
dic.update(dic2)
print(dic)

#4 list - remove duplicate
list = [11,12,13,12,15,16,13]
a = set(list)
print([x for x in a]) # convert to list

#5 fun(args, *kwargs) 不定参数
def demo(args_f, *args_v):
    for x in args_v:
        print(x)

demo("a","b","c","d")