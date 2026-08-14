def match_words(words):
    count = 0
    lst=[]
    for word in words:
        if len(word)>=2 and word[0]==word[-1]:
            count+=1
            lst.append(word)
    print("The list of words that match the criteria is:", lst) 
    return count
count = match_words(["apple", "banana", "civic", "deed", "elephant", "level"])
print("The number of words that match the criteria is:", count)       
   

            