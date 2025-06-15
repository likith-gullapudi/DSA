from os import *
from sys import *
from collections import *
from math import *


class Node:
    def __init__(self):
        self.child = {}
        self.count = {}
        self.end = 0


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        root = self.root
        for i in word:
            root.child[i] = root.child.get(i, Node())
            root.count[i] = root.count.get(i, 0) + 1
            root = root.child[i]
        root.end += 1

    def countWordsEqualTo(self, word):
        root = self.root
        for i in word:
            if root.count.get(i, 0) > 0:
                root = root.child[i]
            else:
                return 0
        return root.end

    def countWordsStartingWith(self, word):
        root = self.root
        for i in word[:-1]:
            if root.count.get(i, 0) > 0:
                root = root.child[i]
            else:
                return 0
        return root.count.get(word[-1], 0)

    def erase(self, word):
        root = self.root
        for i in word:
            root.count[i] = root.count.get(i, 0) - 1
            root=root.child[i]
        root.end-=1

if __name__ == "__main__":
    trie = Trie()

    # Insert multiple overlapping and unique words
    words = ["apple", "app", "application", "apply", "apex", "bat", "batch", "batman", "bats", "cat"]
    for word in words:
        trie.insert(word)
    print("Inserted words:", words)

    # Check counts of exact words
    print("\nExact word counts:")
    for word in ["apple", "app", "application", "bat", "cat", "dog"]:
        print(f"Count of '{word}':", trie.countWordsEqualTo(word))

    # Check counts for prefixes
    print("\nPrefix counts:")
    prefixes = ["app", "bat", "b", "c", "a", "appl"]
    for prefix in prefixes:
        print(f"Count of words starting with '{prefix}':", trie.countWordsStartingWith(prefix))

    # Erase some words
    print("\nErasing words and checking counts:")
    erase_words = ["bat", "apple", "batman", "application"]
    for word in erase_words:
        trie.erase(word)
        print(f"After erasing '{word}':")
        print(f"  Count of '{word}':", trie.countWordsEqualTo(word))
        print(f"  Count of words starting with '{word[:2]}':", trie.countWordsStartingWith(word[:2]))

    # Insert duplicates and check handling
    print("\nInserting duplicates and checking counts:")
    trie.insert("apple")
    trie.insert("apple")
    print("Count of 'apple' after 2 more inserts:", trie.countWordsEqualTo("apple"))
    print("Count starting with 'app' after duplicate inserts:", trie.countWordsStartingWith("app"))


    # Edge case: Non-existing prefix
    print("Count of words starting with 'xyz':", trie.countWordsStartingWith("xyz"))

    # Final validation with mixed operations
    print("\nFinal validation:")
    trie.insert("cat")
    print("Count of 'cat' after reinserting:", trie.countWordsEqualTo("cat"))
    trie.erase("cat")
    print("Count of 'cat' after erasing again:", trie.countWordsEqualTo("cat"))
    trie.insert("catalog")
    print("Count starting with 'cat' after adding 'catalog':", trie.countWordsStartingWith("cat"))
