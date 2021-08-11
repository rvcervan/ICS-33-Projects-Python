import prompt
import goody
from test.datetimetester import pairs

# Use these global variables to index the list associated with each name in the dictionary.
# e.g., if men is a dictionary, men['m1'][match] is the woman who matches man 'm1', and 
# men['m1'][prefs] is the list of preference for man 'm1'.
# It would seems that this list might be better represented as a named tuple, but the
# preference list it contains is mutated, which is not allowed in a named tuple. 

match = 0   # Index 0 of list associate with name is match (str)
prefs = 1   # Index 1 of list associate with name is preferences (list of str)


def read_match_preferences(open_file : open) -> {str:[str,[str]]}:
    singles = {}
    for i in open_file:
        preferences = [None]
        people = i.strip('\n').split(';')
        preferences.append(people[1:])
        singles.update({people[0]:preferences})
    return singles
        
def dict_as_str(d : {str:[str,[str]]}, key : callable=None, reverse : bool=False) -> str:
#     men = sorted(d, key = key, reverse = reverse)
    line = ''
    for x in sorted(d.keys(), key = key, reverse = reverse):
        line += "  {} -> {}\n".format(x, d[x])
    
    return line
    
    
    


def who_prefer(order : [str], p1 : str, p2 : str) -> str:
    if order.index(p2) < order.index(p1):
        return p2
    else:
        return p1


def extract_matches(men : {str:[str,[str]]}) -> {(str,str)}:
    stable = set()
    for i in men.items():
        stable.add((i[0], i[1][0] ))
    return stable


def make_match(men : {str:[str,[str]]}, women : {str:[str,[str]]}, trace : bool = False) -> {(str,str)}:
    dup_men = men.copy()
    unmatched = set()
    print("Women Preferences (Unchanging)")
    print(dict_as_str(women))
    for i in dup_men.items():
        unmatched.add(i[0])
        
        
    while unmatched != set():
        print("Men Preferences (Current)")
        print(dict_as_str(dup_men))
        print("unmatched men = {}".format(unmatched))
        print()
        man = unmatched.pop()
        lady = dup_men[man][1].pop(0)
       
        
        if women[lady][0] == None:
            print("{} proposes to {}, who is currently unmatched, accepting proposal".format(man, lady))
            print()
            women[lady][0] = man
            dup_men[man][0] = lady
            
        else:
            if who_prefer(women[lady][1], man, women[lady][0]) == women[lady][0]:
                print("{} proposes to {}, who is currently matched, rejecting the proposal (likes current match better".format(man, lady))
                print()
                unmatched.add(man)
            else:
                if who_prefer(women[lady][1], man, women[lady][0]) == man:
                    print("{} proposes to {}, who is currently matched, accepting the proposal, rejecting match with {}".format(man, lady, women[lady][0]))
                    print()
                    cheated = women[lady].pop(0)
                    unmatched.add(cheated)
                    women[lady][0] = man
                    dup_men[man][0] = lady
    else:
        print("matches = {}".format(extract_matches(dup_men)))
        
        return extract_matches(dup_men)
        
        
        
  


  
    
if __name__ == '__main__':
#     man_file = goody.safe_open("Choose the file name representing preferences of the men", 'r', 'Invalid')
#     women_file = goody.safe_open("Choose the file name representing preferences of the women", 'r', 'Invalid')
    man_file = open("men0.txt")
    women_file = open("women0.txt")
    print()
    
    man_dict = read_match_preferences(man_file)
    women_dict = read_match_preferences(women_file)
    
    print("Men Preferences")
    print(dict_as_str(man_dict))
    print("Women Preferences")
    print(dict_as_str(women_dict))
    
    make_match(man_dict, women_dict)
    
    
    
    # Write script here
              
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc2.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
