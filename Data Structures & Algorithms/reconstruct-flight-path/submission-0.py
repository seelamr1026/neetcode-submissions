class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        adjList = {src:[] for src,dst in tickets}

        tickets.sort()
        for src,dst in tickets:
            adjList[src].append(dst)
        
        res = ["JFK"]

        def dfs(node):
            if len(res) == len(tickets)+1:
                return True
            if node not in adjList:
                return False
            
            temp = list(adjList[node])
            for i,v in enumerate(temp):
                adjList[node].pop(i)
                res.append(v)
                if dfs(v): return True
                adjList[node].insert(i,v)
                res.pop()
            return False
        
        dfs("JFK")
        return res
        