class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        occurance = defaultdict(int)

        left = 0
        right = 0

        max_length = 0

        while left <= right and right < len(s):
            print(occurance)
            print(left, right, max_length)
            occurance[s[right]] += 1

            max_freq = 0
            total = 0
            for char,freq in occurance.items():
                total += freq
                max_freq = max(freq, max_freq)

            replacements = total - max_freq
            if replacements <= k:
                right += 1
            else:
                max_length = max(max_length, right-left)
                occurance[s[left]] -= 1
                occurance[s[right]] -= 1
                left += 1

        max_length = max(max_length, right-left)

        return max_length
        
            



         