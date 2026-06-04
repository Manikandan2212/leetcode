class Solution:
    def countAndSay(self, n: int) -> str:
        if(n==1):
            return "1"
        elif(n==2):
            return "11"
        string="11"
        for i in range(2,n):
            strs=""
            count=1
            for j in range(1,len(string)):
                if(string[j]==string[j-1]):
                    count+=1
                else:
                    strs+=str(count)+string[j-1]
                    count=1
            strs+=str(count)+string[j]
            string=strs
        return string
                    


        
                        
