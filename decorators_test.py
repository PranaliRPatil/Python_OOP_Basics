#https://www.programiz.com/python-programming/decorator
#https://realpython.com/primer-on-python-decorators/
def my_decorator(func):
  print("Inside decorator")
  func()
  print("End decorator\n*******###*********")

def test_in():
  print("***I m decorator's arg func..!!****")
  # print(num + 1)

# my_decorator(test_in)
@my_decorator   # this is exactly similar to: my_decorator(test_in)
def test_in():
  print("***I m decorator's arg func..!!****")

def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner

@smart_divide
def divide(a, b):
    print(a/b)
divide(10,2)
# This is similar to: divide1 = smart_divide(divide(10,2))
