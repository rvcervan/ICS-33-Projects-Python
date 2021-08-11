import re
from goody import irange
from collections import defaultdict

# Before running the driver on the bsc.txt file, ensure you have put a regular
#   expression pattern in the files repattern1a.txt, repattern1b.txt, and
#   repattern2a.txt. The patterns must be all on the first line

def pages (page_spec : str, unique :  bool) -> [int]: #result in ascending order
    et = page_spec.split(',')
    pattern = r'^([1-9]\d*)(?:([-:])([1-9]\d*)(?:/([1-9]\d*))?)?$'
    page_num = []
    for each in et:
        num_list = []
        m = re.match(pattern, each)
        assert each != None, 'No Match'
        num1, sep, num2, num3 = [i if i != None else None for i in m.group(1,2,3,4)]
        if sep == None:
            num_list.append(int(num1))
        elif sep == '-':
            assert int(num1) <= int(num2), 'pages: in page specification {}, {} > {}'.format(each, num1, num2)
            for i in range(int(num1), int(num2)+1):
                num_list.append(i)
        elif sep == ':':
            for i in range(int(num1), int(num1)+int(num2)):
                num_list.append(i)
        
        if num3 != None:
            num_list = num_list[::int(num3)]
        
        page_num.extend(num_list)
    if unique == True:
        page_num = set(page_num)
        return sorted(list(page_num))
    else:
        return sorted(page_num)
            

    


def expand_re(pat_dict:{str:str}):
    for k,v in pat_dict.items():
        for x, y in pat_dict.items():
            if k in y:
                new = re.sub("#"+k+'#', '(?:'+pat_dict[k.strip('#')]+')', y)
                pat_dict[x] = new




if __name__ == '__main__':
    
    p1a = open('repattern1a.txt').read().rstrip() # Read pattern on first line
    print('Testing the pattern p1a: ',p1a)
    for text in open('bm1.txt'):
        text = text.rstrip()
        print('Matching against:',text)
        m = re.match(p1a,text)
        print(' ','Matched' if m != None else "Not matched")
        
    p1b = open('repattern1b.txt').read().rstrip() # Read pattern on first line
    print('\nTesting the pattern p1b: ',p1b)
    for text in open('bm1.txt'):
        text = text.rstrip()
        print('Matching against:',text)
        m = re.match(p1b,text)
        print('  ','Matched with groups ='+ str(m.groups()) if m != None else 'Not matched' )
        
        
    p2 = open('repattern2a.txt').read().rstrip() # Read pattern on first line
    print('\nTesting the pattern p2: ',p2)
    for text in open('bm2a.txt'):
        text = text.rstrip()
        print('Matching against:',text)
        m = re.match(p2,text)
        print('  ','Matched with groups ='+ str(m.groups()) if m != None else 'Not matched' )
        
    print('\nTesting pages function')
    for text in open('bm2b.txt'):
        text = text.rstrip().split(';')
        text,unique = text[0], text[1]=='True'
        try:
            p = pages(text,unique)
            print('  ','pages('+text+','+str(unique)+') = ',p)
        except:
            print('  ','pages('+text+','+str(unique)+') = raised exception')
        
    
    print('\nTesting expand_re')
    pd = dict(digit = r'[0-9]', integer = r'[+-]?#digit##digit#*')
    print('  Expanding ',pd)
    expand_re(pd)
    print('  result =',pd)
    # produces/prints the dictionary
    # {'digit': '[0-9]', 'integer': '[+-]?(?:[0-9])(?:[0-9])*'}
    
    pd = dict(integer       = r'[+-]?[0-9]+',
              integer_range = r'#integer#(..#integer#)?',
              integer_list  = r'#integer_range#(?,#integer_range#)*',
              integer_set   = r'{#integer_list#?}')
    print('\n  Expanding ',pd)
    expand_re(pd)
    print('  result =',pd)
    # produces/prints the dictionary 
    # {'integer': '[+-]?[0-9]+',
    #  'integer_range': '(?:[+-]?[0-9]+)(..(?:[+-]?[0-9]+))?',
    #  'integer_list': '(?:(?:[+-]?[0-9]+)(..(?:[+-]?[0-9]+))?)(?,(?:(?:[+-]?[0-9]+)(..(?:[+-]?[0-9]+))?))*',
    #  'integer_set': '{(?:(?:(?:[+-]?[0-9]+)(..(?:[+-]?[0-9]+))?)(?,(?:(?:[+-]?[0-9]+)(..(?:[+-]?[0-9]+))?))*)?}'
    # }
    
    pd = dict(a='correct',b='#a#',c='#b#',d='#c#',e='#d#',f='#e#',g='#f#')
    print('\n  Expanding ',pd)
    expand_re(pd)
    print('  result =',pd)
    # produces/prints the dictionary 
    # {'a': 'correct',
    #  'b': '(?:correct)',
    #  'c': '(?:(?:correct))',
    #  'd': '(?:(?:(?:correct)))',
    #  'e': '(?:(?:(?:(?:correct))))',
    #  'f': '(?:(?:(?:(?:(?:correct)))))',
    #  'g': '(?:(?:(?:(?:(?:(?:correct))))))'
    # }
    
    print()
    print()
    import driver
    driver.default_file_name = "bscq2F18.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()