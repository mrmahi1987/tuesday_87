'''
Decorator :
    Decorator is a special function , used to apply/add additional/extra functionality to the existing
    function without changing the exist functions code.

    req :
        . original function.
        . additional functionality with inner function :
            ex :
            outer():
                inner/wrapper():
                    where the actual condition works

        steps :
        pass original function name as argument to the additional function.
        . if original function has argument then we pass that parameter to wrapper function.
        . then do your conditions.
        . in else we need to return original function.
        . in outer function we need to return wrapper() function's address.
        ex : return wrapper #returning functions addres.
        ex : return wrapper() #return functions value.

Implementation :
==============
reference :
def outer():
    def inner():
        print('inner function')
    return inner

outer()
<function outer.<locals>.inner at 0x000001C506893A60>
def outer():
    def inner():
        print('inner function')

outer()

#convert given name into upper based on condition :
#condition : if name is Akhil convert to upper mahesh lower.

def Additional(Original):
    def wrapper(name):
        if name == 'akhil':
            print('Im in upper case : ',name.upper())
        else:
            return Original(name)
    return wrapper


@Additional
def Original(name):
    print('Im in lower case : ',name.lower())

Original("akhil")

#Generator :
Generator is a special function/object , mainly used to save memory space.
means : it captures/identify the state of the object instead store values directly in memory.
It lazily iterates values in a sequence.
. To implement generator in python using "yield keyword".
. Implement generator always in functions only.
. simply : instead of return/print use yield.
. It return generator object : <generator object gen at 0x000001C214ACA500>
ex : Reading large files line by line without loading the whole file into memory.

def gen():
    for i in range(10):
         yield i

#function calling :
print(gen())

output = gen()
print(next(output))
print(next(output))

#ex : 2 :
def func2():
    for i in  [1,2,3,4,5,6,6,7]:
        yield i

out = func2()
print(out)

for i in range(3):
    print(next(out))

'''
#Iterator : next() to get the iterator value, Iterable : ex : all data structures [list,tuple,set ,dict]







