import re, traceback, keyword

def pnamedtuple(type_name, field_names, mutable= False):
    def show_listing(s):
        for line_num, line_text in enumerate(s.split('\n'), 1):
            print(f' {line_num: >3} {line_text.rstrip()}')
            
    def _name_checker(word: str):
        pattern = r'^([^0-9])'
        p = re.compile(pattern)
        m = p.match(word)
        if m == None:
            raise SyntaxError('first index can not be a number')
        else:
            for i in keyword.kwlist:
                if word == i:
                    raise SyntaxError('word can not be a keyword')
        return word
    
    def field_checker(field):
        if type(field) == list:
            for i in field
    
    _name_checker(type_name)
    
    
    class type_name:
        
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self._fields = ['x','y']
            self._mutable = False    
            
                    

    # put your code here
    # bind class_definition (used below) to the string constructed for the class



    # While debugging, remove comment below showing source code for the class
    # show_listing(class_definition)
    
    # Execute this class_definition str in a local name space; then, bind the
    #   source_code attribute to class_defintion; after that try, return the
    #   class object created; if there is a syntax error, list the class and
    #   also show the error
    
    
    name_space = dict(__name__  =  f'pnamedtuple_{type_name}')
    try:
        exec(class_definition,name_space)
        name_space[type_name].source_code = class_definition
    except (TypeError,SyntaxError):   
        show_listing(class_definition)
        traceback.print_exc()
    return name_space[type_name]


    
if __name__ == '__main__':
    # Test pnamedtuple in script below: use Point = pnamedtuple('Point','x,y')
#     Point = pnamedtuple('Point', 'x,y')
#     p = Point(0,0)

    #driver tests
    import driver
    driver.default_file_name = 'bscp3S18.txt'
#     driver.default_show_exception= True
#     driver.default_show_exception_message= True
#     driver.default_show_traceback= True
    driver.driver()
