class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        #initialize empty perms to return in final
        perms = [[]]

        #iterate through each num to be inserted
        for n in nums:
            #iterate through every p in perms
            new_perms = []
            for p in perms:
                #iterate through every index in p
                for i in range(len(p)+1):
                    #create a copy of p and insert i in every index of p and add to new perms
                    p_copy = p.copy()
                    p_copy.insert(i,n)
                    #insert p_copy to new perms
                    new_perms.append(p_copy)
                perms = new_perms
        return perms