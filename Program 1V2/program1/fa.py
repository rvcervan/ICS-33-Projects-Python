import goody


def read_fa(file : open) -> {str:{str:str}}:
    automata = {}
    for i in file:
        num = []
        num_state = []
        con = i.strip('\n').split(';')
        state = con.pop(0)
        while con != []:
            num.append(con.pop(0))
            num_state.append(con.pop(0)) 
        values = zip(num, num_state) 
        automata.update({state: dict(values) })
    return automata
            
        


def fa_as_str(fa : {str:{str:str}}) -> str:
    string = ''
    for i in sorted(fa.items()):
        val = []
        val.extend(sorted(i[1].items()))
        string +="  {} transitions: {}\n".format(i[0], val)
    return string
        
        
def process(fa : {str:{str:str}}, state : str, inputs : [str]) -> [None]:
    print(fa)
    print(state)
    print(inputs)
    print()
    result = []
    state = state
    for i in inputs:
        if state == 'even':
            
        elif state == 'odd':
            pass
            
    


def interpret(fa_result : [None]) -> str:
    pass
        


if __name__ == '__main__':
    file = open("faparity.txt")
    dict_fa = read_fa(file)
    fa_as_str(dict_fa)
    
    inputs = open("fainputparity.txt")
    for i in inputs:
        line = i.strip('\n').split(';')
        process(dict_fa, line[0], line[1:])
    # Write script here
              
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc3.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
