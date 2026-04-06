class Solution:

    def encode(self, strs: List[str]) -> str:
        s=''
        for i in strs:
            s += str(len(i)) + '#' + i
        return s

    def decode(self, s: str) -> List[str]:
        l,i=[],0
        while i<len(s):
            j=i
            while s[j] != '#':
                j += 1
            p=int(s[i:j])
            w=s[j+1:j+p+1]
            l.append(w)
            i=j+p+1
        return l