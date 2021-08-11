# Submitter: rvcervan(Cervantes, Raul)
# Partner  : dapalaci(Palacios, David)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

from goody import type_as_str
import inspect

class Check_All_OK:
    """
    Check_All_OK class implements __check_annotation__ by checking whether each
      annotation passed to its constructor is OK; the first one that
      fails (by raising AssertionError) prints its problem, with a list of all
      annotations being tried at the end of the check_history.
    """
       
    def __init__(self,*args):
        self._annotations = args
        
    def __repr__(self):
        return 'Check_All_OK('+','.join([str(i) for i in self._annotations])+')'

    def __check_annotation__(self,check,param,value,check_history):
        for annot in self._annotations:
            check(param, annot, value, check_history+'Check_All_OK check: '+str(annot)+' while trying: '+str(self)+'\n')


class Check_Any_OK:
    """
    Check_Any_OK implements __check_annotation__ by checking whether at least
      one of the annotations passed to its constructor is OK; if all fail 
      (by raising AssertionError) this classes raises AssertionError and prints
      its failure, along with a list of all annotations tried followed by the
      check_history.
    """
    
    def __init__(self,*args):
        self._annotations = args
        
    def __repr__(self):
        return 'Check_Any_OK('+','.join([str(i) for i in self._annotations])+')'

    def __check_annotation__(self,check,param,value,check_history):
        failed = 0
        for annot in self._annotations: 
            try:
                check(param, annot, value, check_history)
            except AssertionError:
                failed += 1
        if failed == len(self._annotations):
            assert False, repr(param)+' failed annotation check(Check_Any_OK): value = '+repr(value)+\
                         '\n  tried '+str(self)+'\n'+check_history                 



class Check_Annotation:
    # Below, setting the class attribute to True allows checking to occur
    #   (but only if self._checking_on is also True)
    checking_on  = True
  
    # set self._checking_on to True too, for checking the decorated function 
    def __init__(self, f):
        self._f = f
        self._checking_on = True
        
    # Check whether param's annot is correct for value, adding to check_history
    #    if recurs; defines many local function which use it parameters.  
    def check(self,param,annot,value,check_history=''):
        def check_list():
            assert isinstance(value, list), "'{}' failed annotation check(wrong type): value = '{}'\n  was type {} ...should be type {}".format(param, value, type(value), annot)
            if len(annot) == 1:
                for each in value:
                    self.check(param, annot[0], each)
            else:
                assert len(annot) == len(value), "'{}' failed annotation check(wrong number of elements): value = '{}'\n  annotation had {} elements{}".format(param, value, len(annot), annot)
                for i in range(len(annot)):
                    self.check(param, annot[i], value[i])
                    
        def check_tuple():
            assert isinstance(value, tuple), "'{}' failed annotation check(wrong type): value = '{}'\n  was type {} ...should be type {}".format(param, value, type(value), annot)
            if len(annot) == 1:
                for each in value:
                    self.check(param, annot[0], each)
            else:
                assert len(annot) == len(value), "'{}' failed annotation check(wrong number of elements): value = '{}'\n  annotation had {} elements{}".format(param, value, len(annot), annot)
                for i in range(len(annot)):
                    self.check(param, annot[i], value[i])
                    
        def check_dict():
            assert isinstance(value, dict), "'{}' failed annotation check(wrong type): value = '{}'\n  was type {} ...should be type {}".format(param, value, type(value), annot)
            assert len(annot) <= 1
            for k_type, v_type in annot.items():
                for k, v in value.items():
                    self.check(param, k_type, k)
                    self.check(param, v_type, v)
                    
                    
        def check_set():
            assert isinstance(value, set), "'{}' failed annotation check(wrong type): value = '{}'\n  was type {} ...should be type {}".format(param, value, type(value), annot)
            assert len(annot) == 1
            obj = annot.pop()
            for i in value:
                self.check(param, obj, i)
                
            
        def check_fset():
            assert isinstance(value, frozenset), "'{}' failed annotation check(wrong type): value = '{}'\n  was type {} ...should be type {}".format(param, value, type(value), annot)
            assert len(annot) == 1
            for x in annot:
                for i in value:
                    self.check(param, x, i)
        
        def check_lamb():
            assert len(annot.__code__.co_varnames) == 1, "'{}' annotation inconsistency: predicate should have 1 parameter but had {}\n  predicate = {}".format(param, len(annot.__code__.co_varnames), annot)
            try:
                assert annot(value) == True
            except:
                raise AssertionError
        
        def check_rest():
            assert '__check_annotation__' in dir(annot)
            annot.__check_annotation__(self.check, param, value, check_history)
            
        def check_str():
            try:
                assert eval(annot, self._order)
                
            except:
                raise AssertionError
            
        if type(annot) is type:
            assert isinstance(value, annot), "'{}' failed annotation check(wrong type): value = '{}'\n  was type {} ...should be type {}".format(param, value, type(value), annot)
        elif type(annot) is list:
            check_list()
        elif type(annot) is set:
            check_set()
        elif type(annot) is dict:
            check_dict()
        elif type(annot) is tuple:
            check_tuple()
        elif type(annot) is frozenset:
            check_fset()
        elif inspect.isfunction(annot):
            check_lamb()
        elif annot is None:
            pass
        elif type(annot) is str:
            check_str()
        else:
            check_rest()
            
        # Define local functions for checking, list/tuple, dict, set/frozenset,
        #   lambda/functions, and str (str for extra credit)
        # Many of these local functions called by check, call check on their
        #   elements (thus are indirectly recursive)

        # Below, decode check function's annotation; check it against arguments
        
    # Return result of calling decorated function call, checking present
    #   parameter/return annotations if required
    def __call__(self, *args, **kargs):
        
        # Return a dictionary of the parameter/argument bindings (actually an
        #    ordereddict, storing the function header's parameters in order)
        def param_arg_bindings():
            f_signature  = inspect.signature(self._f)
            bound_f_signature = f_signature.bind(*args,**kargs)
            for param in f_signature.parameters.values():
                if not (param.name in bound_f_signature.arguments):
                    bound_f_signature.arguments[param.name] = param.default
            return bound_f_signature.arguments
        self._order = param_arg_bindings()

        if self.checking_on == False and self._checking_on == False:
            return self._f(*args, **kargs)
        # If annotation checking is turned off at the class or function level
        #   just return the result of calling the decorated function
        # Otherwise do all the annotation checking
        
        try:

                        
            annot = self._f.__annotations__
            for key, value in self._order.items():
                if key in annot:
                    self.check(key, annot[key], value)
                    
            result = self._f(*args, **kargs)
            
            if 'return' in annot:
                self._order["_return"] = result
                self.check('return', annot['return'], result)
                
            return result
                    
            
            
            # Check the annotation for all parameters (if there are any)
                    
            # Compute/remember the value of the decorated function
            
            # If 'return' is in the annotation, check it
            
            # Return the decorated answer
            
            #remove after adding real code in try/except
            
        # On first AssertionError, print the source lines of the function and reraise 
        except AssertionError:
#             print(80*'-')
#             for l in inspect.getsourcelines(self._f)[0]: # ignore starting line #
#                 print(l.rstrip())
#             print(80*'-')
            raise




  
if __name__ == '__main__':     
    # an example of testing a simple annotation  
#     def f(x:int): pass
#     f = Check_Annotation(f)
#     f(3)
#     f('a')

    #driver tests
    import driver
    driver.default_file_name = 'bscp4F18.txt'
#     driver.default_show_exception= True
#     driver.default_show_exception_message= True
#     driver.default_show_traceback= True
    driver.driver()
