class Solution:
    def maxFreqSum(self, s: str) -> int:
        v={}
        c={}
        for i in s:
            if i in ['a','e','i','o','u'] and i not in v:
                v[i]=1
            elif i in ['a','e','i','o','u'] and i in v:
                v[i]+=1
            elif i not in ['a','e','i','o','u'] and i not in c:
                c[i]=1
            else:
                c[i]+=1
        max_vowel = max(v.values()) if v else 0
        max_consonant = max(c.values()) if c else 0
        return max_vowel+max_consonant