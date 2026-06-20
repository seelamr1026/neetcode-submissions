class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
        
        adjacencyList = collections.defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                adjacencyList[pattern].append(word)
        
        visit = set()
        visit.add(beginWord)
        queue = deque()
        queue.append(beginWord)

        res = 1

        while queue:
            for i in range(len(queue)):
                word1 = queue.popleft()
                if word1 == endWord:
                    return res                
                for j in range(len(word1)):
                    pattern = word1[:j] + "*" + word1[j+1:]
                    for adjWord in adjacencyList[pattern]:
                        if adjWord not in visit:
                            visit.add(adjWord)
                            queue.append(adjWord)
            res+=1
        return 0
