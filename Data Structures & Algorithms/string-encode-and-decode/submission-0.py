from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        sep = 'Ü'
        encoded = []
        for string in strs:
            size = str(len(string))
            res = size+sep+string
            encoded.append(res)
        return ''.join(encoded)
        
    def decode(self, s: str) -> List[str]:
        current = 0
        res = []
        while current < len(s):
            sep_index = s.find('Ü', current)
            window = int(s[current:sep_index])
            element = s[sep_index+1:sep_index+1+window]
            res.append(element)
            current = sep_index + window + 1
        return res

strs = ["Hello","World"]
s = Solution()
enc = s.encode(strs)
dec = s.decode(enc)
