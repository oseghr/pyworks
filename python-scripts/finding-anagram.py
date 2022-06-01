# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    '''
    The function takes two parameters (words, anagram) and checks if they are anagrams
    '''
    if word == anagram:
        return True
    elif len(word.strip()) == len(anagram.strip()):
        count = 0
        for x in word.strip():
            if x in anagram.strip():
                count += 1
        if count == len(word):
            return True 
        else:
            return False      
    elif len(word) != len(anagram):
        return False

    
 


    
