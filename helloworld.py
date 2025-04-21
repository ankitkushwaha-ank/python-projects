#1
print('hello world')

#2
a= 'hello world'
print(a)

#3
a = 'hello'
b = 'world'
print(a+ ' ' +b)
#4
def fun():
    a =' hello world'
    print(a)
fun()

#5
hello = 'hello world '
for i in hello:
    hello.strip()
    print(i)

#6
# while True:
#     hello = 'hello world '
#     for i in hello:
#         hello.strip()
#         print(i)

#7
print('''
hello world
''')

#8
print('hello \nworld')

#9


def fun():
    a = 12
    b = 13
    c = a + b
    print(c)
fun()

def fun2(a , b):
    return a + b


result = fun2(4 , 5)
print(result)
