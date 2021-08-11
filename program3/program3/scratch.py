import re, keyword
def type_name_checker(word: str):
        pattern = r'^([^0-9])'
        p = re.compile(pattern)
        m = p.match(word)
        print(m)
        print()
        for i in keyword.kwlist:
            print(i)
        
type_name_checker('1uyg')