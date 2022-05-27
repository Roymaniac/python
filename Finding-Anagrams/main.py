# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    sort1 = word.lower()
    sort2 = anagram.lower()
    if sorted(sort1) == sorted(sort2):
        print("True")
    else:
        print("False")


find_anagram("binary", "Brainy")
find_anagram("Binary", "brainy")
find_anagram("hello", "check")
find_anagram("below", "elbow")
