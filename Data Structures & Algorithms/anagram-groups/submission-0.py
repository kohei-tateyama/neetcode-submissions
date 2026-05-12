class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for i in range(0,len(strs)):
            sorted_str = "".join(sorted(strs[i]))

            if sorted_str not in hash_map:
                hash_map[sorted_str] = []
            
            hash_map[sorted_str].append(strs[i])
        return list(hash_map.values())