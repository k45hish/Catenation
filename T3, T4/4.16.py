def foo():
        try:
            print("x")
            return 2    
        finally:
            print("y")
            return 2
k = foo()
print(k)

#if indentation error is fixed both blocks will run. Try block will return value as 1 but finally block will overwrite its value as 2 
# and output will be 2

def a():
    try:
        f(x, 4)
    finally:
        print('after f')
        print('after f?')
a()

#if indentation error is fixed there will be a NameError as f is not defined. 