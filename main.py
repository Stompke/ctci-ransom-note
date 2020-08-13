# https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps


"""
UPER:

U:
    > 2 arrays
    > Check if first array (magazine) has all the words in the second array (note)
    > Case-sensitive

P:
    > Iterate through all items in the "note" array
        > Add each word to a cache
    > Iterate through "magazine" array
        > If magazine word is in cache
            > add 1 to a counter
    > If counter == len(note)
        > Return Yes
    > else
        > Return No

E:
    > CODE👨‍💻

"""

def checkMagazine(magazine, note):
    cache = {}

    # Add words to cache from ransom note. Also count how many of each word.
    for word in note:
        if word in cache:
            cache[word] = cache[word] + 1
        else:
            cache[word] = 1
    
    # Decrement or Remove word from cache if word matches
    for word in magazine:
        if word in cache:
            if cache[word] > 1:
                cache[word] = cache[word] - 1
            else:
                del cache[word]
            
        # Whenever cache is empty, all words have been found. Print Yes
        if len(cache) == 0:
            print("Yes")
            return True

    # All words were not found, Print No
    print("No")
    return False
    
    





checkMagazine('hihi',';lja')