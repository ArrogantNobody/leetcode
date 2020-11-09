class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = dict()
        for s in strs:
            t = "".join(sorted(s))
            print(t)

        #     if t in hashmap:
        #         hashmap[t].append(s)
        #     else:
        #         hashmap[t] = [s]
        #
        # return hashmap.values()

if __name__ == '__main__':
    s = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    s.groupAnagrams(strs)