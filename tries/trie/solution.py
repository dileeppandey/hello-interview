from collections import defaultdict
import unittest as ut


class Trie:
    """
    Basic implementation of Trie with insert and search operation.
    """

    def __init__(self):
        # ------------------------------------------------------------------
        # TRIE INSIGHT: A Trie (prefix tree) uses a tree where each node 
        # represents a character. This allows for O(L) insertion and 
        # search (where L is the word length), regardless of the total 
        # number of words in the Trie.
        # ------------------------------------------------------------------
        self.head = defaultdict()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        # Step 1: Start at the root node
        current = self.head
        
        # Step 2: Traverse character by character
        for letter in word:
            # Step 3: Use setdefault to move to the next level, 
            #         creating a new dictionary if it doesn't exist
            current = current.setdefault(letter, {})
            
        # Step 4: Mark the end of the word
        current.setdefault("END")

    def search(self, word: str) -> bool:
        """
        Return True if word in Trie, else False.
        """
        # Step 1: Start at the root node
        current = self.head
        
        # Step 2: Traverse character by character
        for letter in word:
            # Step 3: If a character is missing, the word isn't there
            if letter not in current:
                return False
            current = current[letter]
            
        # Step 4: A word is found only if we've reached an "END" marker
        return "END" in current


class Test(ut.TestCase):
    def test_insert(self):
        trie = Trie()
        trie.insert("word")
        self.assertDictEqual(
            trie.head, {'w': {'o': {'r': {'d': {'END': {}}}}}})

    def test_search(self):
        trie = Trie()
        trie.insert("word")
        trie.insert("world")
        self.assertEqual(trie.search("word"), True)
        self.assertEqual(trie.search("world"), True)
        self.assertEqual(trie.search("wor"), False)
        self.assertEqual(trie.search("words"), False)


if __name__ == "__main__":
    ut.main()
