class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for string in strs:
            encoded += str(len(string)) + '#' + string

        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []

        i = 0
        delimiter = '#'

        while i < len(s):
            length = 0
            while i < len(s) and s[i] != '#':
                length = length*10 + int(s[i])
                i += 1

            i += 1

            decoded.append(s[i:i+length])

            i += length

        return decoded

    
