graph = [
    [0,4,4,0,0,0],  
    [0,0,2,3,6,1],  
    [4,2,0,0,0,1],  
    [0,3,0,0,2,0], 
    [0,6,0,2,0,3],  
    [0,1,0,0,3,0],  
]
names = ["S","A","B","C","D","E"]
LIMIT = 2

def dls_iter(start):
    visited = [False]*len(graph)       
    stack = [(start, 0)]
    while stack:
        node, depth = stack.pop()
        if not visited[node]:
            visited[node] = True
            print(f"Discovered {names[node]} at depth {depth}")

            if depth < LIMIT:
                for nbr in reversed(range(len(graph))):  
                    if graph[node][nbr] != 0 and not visited[nbr]:
                        stack.append((nbr, depth + 1))

def main():
    print(f"Depth-Limited Search (limit={LIMIT}), starting at S:")
    dls_iter(0)  

if __name__ == "__main__":
    main()
