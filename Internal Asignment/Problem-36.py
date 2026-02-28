#Given an array of strings strs, group the anagrams together. You can return the answe#Given an array of strings strs, group the anagrams together. You can return the answer in any order. 

def groupAnagrams(strs):
    anagrams = {}
    
    for word in strs:
        key = ''.join(sorted(word))
        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(word)
    
    return list(anagrams.values())

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"])) #output = [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]