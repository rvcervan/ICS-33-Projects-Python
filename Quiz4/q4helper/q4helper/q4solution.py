# Generators must be able to iterate through any kind of iterable.
# hide is present and called to ensure that your generator code works on
#   general iterable parameters (not just a string, list, etc.)
# For example, although we can call len(string) we cannot call
#   len(hide(string)), so the generator functions you write should not
#   call len on their parameters
# Leave hide in this file and add code for the other generators.

def hide(iterable):
    for v in iterable:
        yield v


# The combination of return and yield None make each of the following
#   a generator (yield None) that immediately raises the StopIteration
#   exception (return)

def sequence(*iterables):
    
    for i in iterables:
        for x in i:
            yield(x)
#     return
#     yield None


            
def group_when(iterable,p):
    letters = []
    try:
        for i in iterable:
            if p(i) == False:
                letters.append(i)
                 
            elif p(i) == True:
                letters.append(i)
                give = letters
                letters = []
                yield give
    finally:
        if letters != []:
            yield letters
#     return
#     yield None

    
                
def drop_last(iterable,n):
    stuff = [x for x in iterable]
    hidden = iter(stuff)
    for i in range(len(stuff)-n):
        x = next(hidden)
        yield x
    #
        
        
#     return
#     yield None


        
def yield_and_skip(iterable,skip):
    hidden = iter(iterable)
    try:
        while True:
            i = next(hidden)
            yield(i)
            for x in range(skip(i)):
                next(hidden)
    except StopIteration:
        pass
    finally:
        del hidden
#     return
#     yield None



        
def alternate_all(*args):
#     stuff = [x for x in args]

    
    for i in args:
        hidden = iter(i)
        char = next(hidden)
        print(char)

            
    
#     return
#     yield None




def min_key_order(adict):
    numbers = []
    for k, v in adict.items():
        numbers.append(k)
    print(numbers)
    yield None
    return

 
           
         
if __name__ == '__main__':
    from goody import irange
    
    # Test sequence; you can add any of your own test cases
    print('Testing sequence')
    for i in sequence('abc', 'd', 'ef', 'ghi'):
        print(i,end='')
    print('\n')

    print('Testing sequence on hidden')
    for i in sequence(hide('abc'), hide('d'), hide('ef'), hide('ghi')):
        print(i,end='')
    print('\n')


    # Test group_when; you can add any of your own test cases
    print('Testing group_when')
    for i in group_when('combustibles', lambda x : x in 'aeiou'):
        print(i,end='')
    print('\n')

    print('Testing group_when on hidden')
    for i in group_when(hide('combustibles'), lambda x : x in 'aeiou'):
        print(i,end='')
    print('\n')


    # Test drop_last; you can add any of your own test cases
    print('Testing drop_last')
    for i in drop_last('combustible', 5):
        print(i,end='')
    print('\n')

    print('Testing drop_last on hidden')
    for i in drop_last(hide('combustible'), 5):
        print(i,end='')
    print('\n')


    # Test sequence; you can add any of your own test cases
    print('Testing yield_and_skip')
    for i in yield_and_skip('abbabxcabbcaccabb',lambda x : {'a':1,'b':2,'c':3}.get(x,0)):
        print(i,end='')
    print('\n')

    print('Testing yield_and_skip on hidden')
    for i in yield_and_skip(hide('abbabxcabbcaccabb'),lambda x : {'a':1,'b':2,'c':3}.get(x,0)):
        print(i,end='')
    print('\n')


    # Test alternate_all; you can add any of your own test cases
    print('Testing alternate_all')
    for i in alternate_all('abcde','fg','hijk'):
        print(i,end='')
    print('\n')
    
    print('Testing alternate_all on hidden')
    for i in alternate_all(hide('abcde'), hide('fg'),hide('hijk')):
        print(i,end='')
    print('\n\n')
       
         
#     Test min_key_order; add your own test cases
#     print('\nTesting Ordered')
#     d = {1:'a', 2:'x', 4:'m', 8:'d', 16:'f'}
#     i = min_key_order(d)
#     print(next(i))
#     print(next(i))
#     del d[8]
#     print(next(i))
#     d[32] = 'z'
#     print(next(i))
#     print(next(i))
#     


         
         
    import driver
    driver.default_file_name = "bscq4F18.txt"
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
    
