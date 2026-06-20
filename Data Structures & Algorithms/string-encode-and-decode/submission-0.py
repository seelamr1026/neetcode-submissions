class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == []:
            return ""
        
        sizes = []
        for s in strs:
            sizes.append(len(s))
        
        res = ""
        for size in sizes:
            res+=str(size)
            res+=","
        res+="#"
        for s in strs:
            res+=s
        return res

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        sizes = []
        final = []
        i=0
        while s[i]!="#":
            curr = ""
            while s[i]!=",":
                curr+=s[i]
                i+=1
            sizes.append(int(curr))
            i+=1
        i+=1
        for sz in sizes:
            final.append(s[i:i+sz])
            i+=sz

        return final        
