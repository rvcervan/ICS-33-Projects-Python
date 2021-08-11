from collections import defaultdict
from goody import type_as_str
import prompt
from builtins import int

class Bag:
    def __init__(self, bagging):
        self.b = defaultdict(int)
        for obj in bagging:
            self.b[obj] += 1
    
    def __repr__(self):
        unbag = [k * v for k, v in self.b.items()]
        second = [x for i in unbag for x in i]
        return "Bag({})".format(second)

    def __str__(self):
        com = ''
        for k, v in self.b.items():
            com += '{}[{}], '.format(k, v)
        com = com.strip(', ')
        return "Bag(" + com + ")"
    
    def __len__(self):
        count = 0
        for k, v in self.b.items():
            count += v
        return count
           
    def unique(self):
        count = 0
        for k, v in self.b.items():
            count += 1
        return count
            
        
        
        
    
    def __contains__(self, obj: str) -> bool:
        if obj in self.b:
            return True
        else:
            return False
    
    def count(self, obj: str) -> int:
        if obj in self.b:
            return self.b[obj]
        else:
            return 0
    
    def add(self, obj: str):
        if obj in self.b:
            for k, v in self.b.items():
                self.b[k] = v+1
        else:
            self.b[obj] = 1
    
    def __add__(self, bag):
        bag1 = self.b
        oldbag2 = bag
        bag2 = defaultdict(int)
        for obj in oldbag2:
            bag2[obj] += 1
        print(bag1)
        print(bag2)
        
        
            





if __name__ == '__main__':
    b = Bag(['d','a','d','b','c','b','d'])
    c = Bag(['o', 'x'])
    print(b.b)
    print(b.__repr__())
    print(b.__str__())
    print(b.__len__())
    print(b.unique())
    print(b.__contains__('z'))
    print(b.__contains__('a'))
    print(b.count('o'))
    print(b.count('d'))
    b.add('d')
    b.add('o')
    print(b.count('o'))
    print(b.count('d'))
    print(b.unique())
#     print(b.__add__(c))
    b.__add__(c)
    
    print('------------------------------------------------')
    
    #Simple tests before running driver
    #Put your own test code here to test Bag before doing the bsc tests
    #Debugging problems with these tests is simpler

    b = Bag(['d','a','d','b','c','b','d'])
    print(repr(b))
    print(all((repr(b).count('\''+v+'\'')==c for v,c in dict(a=1,b=2,c=1,d=3).items())))
    for i in b:
        print(i)

    b2 = Bag(['a','a','b','x','d'])
    print(repr(b2+b2))
    print(str(b2+b2))
    print([repr(b2+b2).count('\''+v+'\'') for v in 'abdx'])
    b = Bag(['a','b','a'])
    print(repr(b))
    print()
    
    import driver
    driver.default_file_name = 'bscp21F18.txt'
#     driver.default_show_exception = prompt.for_bool('Show exceptions when testing',True)
#     driver.default_show_exception_message = prompt.for_bool('Show exception messages when testing',True)
#     driver.default_show_traceback = prompt.for_bool('Show traceback when testing',True)
    driver.driver()
