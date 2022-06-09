def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)
print(are_anagrams("nameless", "salesmen"))
