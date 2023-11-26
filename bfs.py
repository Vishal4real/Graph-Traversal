graph = {1:[2,3],2:[3],3:[4,7],4:[5,6],7:[],5:[],6:[]}
visited = []
queue = []

def bfsfun(visited,queue,root):
    queue.append(root) # QUEUE 1
    while queue: #TRUE
        m =queue.pop(0) # M =1 QUEUE EMPTY
        visited.append(root) # VISITED =1
        print(m, end = " ") #1 
        
        for adjnode in graph[m]:
            if adjnode not in visited: #VISITED = 1
                visited.append(adjnode) #VISITED = 1 , 2 ,3
                queue.append(adjnode) # 2,3
                
print("This is BFS example")
bfsfun(visited,queue,1)