class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_list = {}
        for i, w in enumerate(strs):
            w = sorted(w)
            w = ''.join(w)
            sorted_list[i] = w
        hash_map = {}
        for k,v in sorted_list.items():
            key = v
            if key not in hash_map:
                hash_map[key] = []
            hash_map[key].append(k)
        anagrams = []
        for v in hash_map.values():
            group = []
            for i in v:  
                group.append(strs[i])
            anagrams.append(group)
        return anagrams
       