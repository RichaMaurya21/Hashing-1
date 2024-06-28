'''## Problem 1:
Given an array of strings, group anagrams together.

Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]'''

class Solution:
    def groupAnagrams(self, strs):
        # Assigning a unique prime number to each letter
        primes = {
            'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11,
            'f': 13, 'g': 17, 'h': 19, 'i': 23, 'j': 29,
            'k': 31, 'l': 37, 'm': 41, 'n': 43, 'o': 47,
            'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71,
            'u': 73, 'v': 79, 'w': 83, 'x': 89, 'y': 97,
            'z': 101
        }
        
        # Dictionary to store grouped anagrams
        anagrams = {}
        
        for word in strs:
            # Calculate the product of primes for the word
            product = 1
            for char in word:
                product *= primes[char]
            
            # Group anagrams by their product using get
            anagrams[product] = anagrams.get(product, []) + [word]
        
        return list(anagrams.values())
sol = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = sol.groupAnagrams(strs)
print(result)