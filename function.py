def run_X_times(times):
    def outer_wrapper(func):
        def inner_wrapper(*args, **kwargs):
            for i in range(times):
                func(*args, **kwargs)
        return inner_wrapper
    return outer_wrapper

@run_X_times(10)
def hello(name):
    print(f'hello {name}')

@run_X_times(5)
def ololo():
    print('ololo')

# hello = run_10_times(hello)

hello('caiman')
print()
ololo()