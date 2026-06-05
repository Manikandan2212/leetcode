class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        n=len(name)
        m=len(typed)
        if n>m or name[0]!=typed[0]:
            return False
        i,j=1,1
        while(j<m):
            if(i<n and name[i]==typed[j]):
                i+=1
                j+=1
            elif typed[j]==typed[j-1]:
                j+=1
            else:
                return False
        if name[n-1]!=typed[m-1] or i<n:
            return False
        return True