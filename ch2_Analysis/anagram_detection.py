def anagramSolution1(s1,s2):
    list_s2 = list(s2)
    pos1 = 0
    stillOK = True
    
    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        
        while pos2 < len(list_s2) and not found:
            if s1[pos1] == list_s2[pos2]:
                found = True
            else:
                pos2 += 1
        if found:
            list_s2[pos2] = None
        else:
            stillOK = False
        pos1 += 1
        
    return stillOK

def anagramSolution2(s1, s2):
    list_s1 = list(s1)
    list_s2 = list(s2)
    
    list_s1.sort()
    list_s2.sort()
    
    pos = 0
    matches = True
    
    while pos < len(s1) and matches:
        if list_s1[pos] == list_s2[pos]:
            pos += 1
        else:
            matches = False
    
    return matches

def anagramSolution3(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26
    
    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] += 1
        
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] += 1  
        
    index = 0
    stillOK = True
    while index < 26 and stillOK:
        if c1[index] == c2[index]:
            index += 1
        else:
            stillOK = False
    
    return stillOK



print(anagramSolution1("earth","heart"))
print(anagramSolution1("earth","heamt"))

print(anagramSolution2("earth","heart"))
print(anagramSolution2("earth","heamt"))

print(anagramSolution3("earth","heart"))
print(anagramSolution3("earth","heamt"))

                
            