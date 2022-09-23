def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    for s in strs:
        split = s.split()
        strs[strs.index(s)] = split
    print(strs)
    return strs


groupAnagrams(["end", "else"])


