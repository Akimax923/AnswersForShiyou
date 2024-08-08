def min_sequences(source, target):
    source_set = set(source)
    if any(char not in source_set for char in target):
        return -1
    count = 0
    i=0 # target index
    while i<len(target):
        j=0 # source index
        while i<len(target) and j<len(source):
            if target[i]==source[j]:
                i += 1
            j += 1
        count += 1
    #print(source_set)
    if count==0:
        return -1
    return count
#min_sequences("abc", "abcbc")
print(min_sequences("abc", "abcbc"))  # 输出: 2
print(min_sequences("cabd", "acdbc"))  # 输出: -1
print(min_sequences("xyz", "xzyxz")) 