#graph search with width prior search and deque
graph={}
graph['you']=['alice','bob','claire']
graph['bob']=['anuj','peggy']
graph['alice']=['peggy']
graph['claire']=['thom','jonny']
graph['anuj']=[]
graph['peggy']=[]
graph['thom']=[]
graph['jonny']=[]

from collections  import deque
def  search(name):
    search_queue=deque()   #create a deque()
    search_queue+=graph[name]  #add input as the first index
    searched=[]
    while search_queue:
        person = search_queue.popleft()   
        if person not in searched:
            
            if person_is_seller(person):
                print(person+' is a mango seller.')
                return True
            else:
                search_queue +=graph[person]
                searched.append(person)
    return False
def person_is_seller(name):
    return name[-1]=='m'
print(search('you'))
print(search('alice'))
