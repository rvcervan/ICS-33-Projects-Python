# Submitter: rvcervan(Cervantes, Raul)
# Partner  : dapalaci(Palacios, David)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

import goody
import prompt
from collections import defaultdict


def read_graph(file : open) -> {str:{str}}:
    maps = []
    for k in file:
        maps.append(k[0]+k[2])
        
    nodes = defaultdict(set)
    
    for key, value in maps:
        nodes[key].add(value)
    
    return nodes
        
def graph_as_str(graph : {str:{str}}) -> str:
    print("Graph: any node -> [all that node's destination nodes]")
    all = ''
    for key, value in sorted(graph.items()):
        each = ('  {} -> {}\n'.format(key, sorted(value)))
        all += each
                 
    return all
       
def reachable(graph : {str:{str}}, start : str, trace : bool = False) -> {str}:
    reached_set = set()
    exploring_list = [start]
     
    while exploring_list != []:
        
        if trace == True:
            upper_script(reached_set, exploring_list)
        
        key = exploring_list.pop(0)
        if trace == True:
            mid_script(key)
        
        if key not in reached_set:
            reached_set.add(key)            
            value = graph.get(key, '')
            
            for paths in value:
                exploring_list.append(paths)
                
        if trace == True:
            bottom_script(key, exploring_list)
                       
    return reached_set

def upper_script(reached: set(), exploring_list: list):
    print("reached set    = {}\nexploring list = {}".format(reached, exploring_list))

def mid_script(key):
    print("removing node from exploring list and adding it to reached list: node = {}".format(key))

def bottom_script(key, Updated_ep):
    print("after adding all nodes reachable directly from {} but not already in reached, exploring = {}".format(key, Updated_ep))
    print()
    

def askr(graph: dict()):
    while True:
        start = input('Choose the start node (or choose quit): ')
        
        if start == 'quit':
            return start
        elif start not in graph.keys():
            print("  Entry Error: '{}'; Illegal: not a source node\n  Please enter a legal String\n".format(start))
        else:
            return start


if __name__ == '__main__':    
    file = goody.safe_open('Choose the file name representing the graph', 'r', "Invalid file name, try another one")
    the_graph = read_graph(file)
    print()
    print(graph_as_str(the_graph))
    
    while True:
    
        start = askr(the_graph)     
    
        if start == 'quit':
            break
            
        trace = prompt.for_bool('Choose whether to trace this algorithm[True]')
        reached = reachable(the_graph, start, trace)
        if trace == False:
            print('From {} the reachable nodes are {}'.format(start, reached))
            print()
    
              
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc1.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
