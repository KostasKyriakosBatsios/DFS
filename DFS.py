import random as rn

def rn_init(l, nl):
    index = nl.pop(rn.randint(0, l - 1)) # pick a random number from 0 to the length of the list - 1 (0 index, that's why we remove by 1, otherwise we've overflow)
    l = len(nl) # we get the new length of our list
    return index, l, nl # return the letter we got randomly, the current length of the list, and the new node list

def dfs(graph, beggining, goal):
    visited = list() # Keeping track of visited nodes
    stack = [(beggining, [beggining])] # Storing nodes and it's path (Stack is LIFO = Last In First Out)

    while stack:
        current_node, path = stack.pop() # Getting the current node and it's path

        # If the current node is our target, return the founded target, the path from start to target, and all visited nodes 
        if current_node == goal:
            visited.append(current_node)
            return current_node, path, visited
        
        # If the current node has not been visited, visit it
        if current_node not in visited:
            visited.append(current_node)

            # Visiting the neighbors and add them to the stack
            for neighbor in reversed(graph[current_node]):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

    # If the target hasn't been found, return None
    return None, [], visited

# List with all of the nodes and it's length
nodes_list = ['A', 'B', 'C', 'D', 'E', 'F', 'I', 'G1', 'G2', 'G3'] 
length = len(nodes_list)

# Initializing our sublists
list1 = list()
list2 = list()
list3 = list()
list4 = list()
list5 = list()
list6 = list()
list7 = list()

# Giving values (the nodes from our nodes list) to our sublists
while length > 0:
    i, length, nodes_list = rn_init(length, nodes_list)
    if i == 'A':
        list1.append(i)
        list3.append(i)
    elif i == 'B':
        list1.append(i)
        list2.append(i)
    elif i == 'C':
        list3.append(i)
        list5.append(i)
    elif i == 'D':
        list1.append(i)
        list7.append(i)
    elif i == 'E':
        list5.append(i)
    elif i == 'F':
        list4.append(i)
    elif i == 'I':
        list4.append(i)
        list5.append(i)
    elif i == 'G1':
        list2.append(i)
    elif i == 'G2':
        list4.append(i)
    elif i == 'G3':
        list6.append(i)
        list7.append(i)

# Our graph adjacency (final form) ("dynamically")
gadj = {
    'I': list1,
    'A': list2,
    'B': list3,
    'C': list4,
    'D': list5,
    'E': list6,
    'F': list7,
    'G1': [],
    'G2': [],
    'G3': []
}

# Our graph adjacency (final form) ("statically")
"""gadj = {
    'I': ['A', 'B', 'D'],
    'A': ['B', 'G1'],
    'B': ['A', 'C'],
    'C': ['F', 'I', 'G2'],
    'D': ['C', 'E', 'I'],
    'E': ['G3'],
    'F': ['D', 'G3'],
    'G1': [],
    'G2': [],
    'G3': []
}"""


print(gadj) # print the graph, so we can see how each node's neighbors are shown

root = 'I' # Our root node
targets = ['G1', 'G2', 'G3'] # Our list with all the target nodes
target = targets[rn.randint(0, 2)] # Getting randomly the target we want to find

result, path, visited = dfs(gadj, root, target) # Executing the Depth First Search (DFS)

# If we've found our target, print: the target, it's path from root to target, and all nodes that have been visited
if result:
    print(f"Target node found: {result}")
    print(f"Entire path (root -> target): {path}")
    print(f"All nodes visited: {visited}")
# Else, print an appropriate message
else:
    print("The target has not been found")