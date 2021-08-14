# def _prin_(var str){
#     print("测试")
# }
# 变量
'''
my_name = 'chuanbei'
print(my_name)
my_name = 1
print(my_name)
'''

# 数据类型
'''
num1 = 1
num2 = 1.1
str1 = 'xxx'
b = True

C = [10, 20, 30]
d = (10, 20, 30)
e = {10, 20, 30}
f = {'name': 'tom', 'age': '123'}
print(type(num1))
print(type(num2))

print(type(str1))
print(type(b))
print(type(C))
print(type(d))
print(type(e))
print(type(f))
'''
# 格式化输出
'''
strGeShihua = "a"
fds= 12312.1231
print("字符串%s，\n\t值域%3f.3" %(strGeShihua, fds), end="xx")
value = input("输入")
print(value)
'''
# 运算
'''
print( 10//3)
print(2**10)
numbers1=10
numbers1 +=1
print(numbers1)
'''
# if
''' 
a = 0
b = 3
c = 2

print(a > b and b < c)
print(b or c)
print(b and c)

if a > b:
    print("大于成立")
elif b > c:
    print("大于还是成立")
    if not a > b:
        print("a不大于b")
else:
    print("大于不成立")
print("大于还是成立")

d = b if a>b else a
print(d)
'''
# 循环语句 九九乘法
'''
a = 1
b = 1
while a <= 9:
    while b <= 9:
        if b <= a:
            print("%d * %d = %d \t" % (a, b, a * b), end="")
            b += 1
        else:
            a += 1
            b = 1
            print("\n")
            
            
fornum = "11111111113333as"
for a in fornum:
    print("数值a%s" % a)
'''

# 字符串
'''
a = 'xx'
b = "dsf"
c = 'ds' 
print(type(a))
print( b )
print(type(c))
print(c)

print(b[2])
#切片
str = " 江山如此多娇，引无数英雄竞折腰 江山 "
strword = "hello world"
print(str[-1:-5:-1])
#查找
index = str.find('如此',1,8)
print(str.count('如此',1,28))
print(str.index('英雄',1,28))
print(str.strip())
print(str.join("Hh"))
print(str.replace("江山","美人",1))
print(str)
print(strword.rstrip())
print(strword.center(20,'*'))
print(strword.startswith("hell2"))
print(strword.endswith("worlds"))
print(strword.isalpha())
print(strword.isalnum())
print(strword.isdigit())
print(strword.isspace())
'''
# 列表
'''
list = ["TOM", "TIMi", "ROSE", "LEI", 5, 6, 1]

print(list.index('TIMi'))
print(list.count(1))
print(len(list))
print('ROSEx' not in list)
list.append("xxx")
list.insert(0, "xxx")
print(list)
list.extend(["eew", "word"])
print(list)
del (list[3])
print(list)
list.remove(1)
print(list)
list1 = [2, 3, 6, 3, 6, 2, 3, 4]
list1.sort(reverse=True)
print(list1)
listcopy = list.copy()
listcopy[1] = "tihuan"
print(listcopy)

# i=0
# while i < len(list):
#     print(list[i])
#     i+=1
# for i in list:
#     print(i)
# name_list = [["xiaomi", "xiaohong"], ["张山", "李四"]]
# for i in name_list:
#     for j in i:
#         print("第%d值为%d" % (name_list[i], j))
'''
# 元组
'''
t1 = (1, 2, 3, "x")
print(t1.count(2))
print(t1.index(3))
print(len(t1))
t2=(1,2,["x","y"])
t2[2][1] ="xy"
print(t2)
'''
# 字典
'''
dict1 = {"name": "tom", "age": 78, "sex": "男"}
print(dict1)
print(len(dict1))
print(dict())
dict1["name"] = "ROSE"
dict1["id"] = 123
dict1["id"] = 12321
del dict1["age"]
print(dict1.get("name"))
for key,value in dict1.items():
    print(f"{key} ={value}")
'''
# 集合
'''
s1 = {10, 20, 20, 30}
print(s1)
s2 =set('abcdefg')
print(s2)
s3 =set()
print(s3)
s1.add(30)
print(s1)
s1.remove(30)
s1.update({50,90})
print(s1)
s1.pop()
print(s1)
s1.discard(100)
print(s1)

for index in s1:
    print(index)
print( 10 in  s1)


for index in range(1,10,3):
    print(index)

for index in enumerate(s1):
    print(index)
tupleStr = tuple(s1)
print(tupleStr)

listRange = {i:j*j for i in range(10) for j in range(1,10,2)}
print(listRange)
'''
#函数
'''
global a
a = 100


def fun():
    # global a
    # a = 1323
    return a


def fun1():
    
    a = 132311
    return a


print(fun())
print(fun1())
print(a)
'''
# 引用
a = "1"
b = a

a.replace("1","342")
print(id(a))
print(id(b))
print(a)
print(b)
