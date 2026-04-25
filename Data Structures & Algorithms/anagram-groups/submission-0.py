class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaGroups = {}

        for i in range(len(strs)):
            s = strs[i]
            sortedString  = str(sorted(s))
            # print(sortedString)

            if sortedString in anaGroups:
                anaGroups[sortedString].append(s)
            else:
                anaGroups[sortedString] = [s]

        groups = []

        for k in anaGroups:
            groups.append(anaGroups[k])

        return groups