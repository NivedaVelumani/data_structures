#it is representated in ADjancency List Representation

def add_node(v):
    if v in graph:
        print(v,"Node is already present")
    else:
        graph[v]=[]

def add_edge(v1,v2):
    if v1 not in graph:
        print(v1,"is not present in the graph")
    elif v2 not in graph:
        print(v2,"is not present in the graph")
    else:
        # list1=[v2,cost]
        # list2=[v1,cost]
        graph[v1].append(v2)
        graph[v2].append(v1)

def delete_node(v):
     if v not in graph:
        print(v,"Node is not present")
     else:
         graph.pop(v)
         for i in graph:
             list1=graph[i]
             for j in list1:
                 if v==j[0]:
                     list1.remove(j)
                     break
            #  if v in list1:
            #      list1.remove(v)

def delete_edge(v1,v2):

    if v1 not in graph:
        print(v1,"is not present in the graph")
    elif v2 not in graph:
        print(v2,"is not present in the graph")
    else:
        if v2 in graph[v1]:
            graph[v1]=remove[v2]
            graph[v2]=remove[v1]
     


         






graph={}
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")

add_edge("A","B")
add_edge("B","E")
add_edge("A","C")
add_edge("A","D")
add_edge("B","D")
add_edge("C","D")
add_edge("E","D")

delete_node("C")
delete_edge("C","D")
# delete_node("A")
print(graph)