def groupAnagrams(strs: list[str]) -> list[list[str]]:
    out = []
    done = []
    for i in range(len(strs)):
        if i not in done:
            i_list = [strs[i]]
            done.append(i)
            for j in range(i+1, len(strs)):
                if set(strs[i]) == set(strs[j]) and j not in done:
                    i_list.append(strs[j])
                    done.append(j)                
            out.append(i_list)
    return out


strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))