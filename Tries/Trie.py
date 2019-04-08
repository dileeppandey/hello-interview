from collections import defaultdict
import unittest as ut


class Trie:
    """
    Basic implementation of Trie with insert and search operation.
    """

    def __init__(self):
        self.head = defaultdict()

    def insert(self, word):
        """
        Inserts a word into the trie
        """
        current = self.head
        for letter in word:
            current = current.setdefault(letter, {})
        current.setdefault("END")

    def search(self, word):
        """
        Return True if word in Trie, else False
        """
        current = self.head
        for letter in word:
            if letter not in current:
                return False
            current = current[letter]
        if "END" in current:
            return True
        return False


class Test(ut.TestCase):
    def test_insert(self):
        trie = Trie()
        trie.insert("word")
        print(trie.head)
        self.assertDictEqual(
            trie.head, {'w': {'o': {'r': {'d': {'END': None}}}}})

    def test_search(self):
        trie = Trie()
        trie.insert("word")
        self.assertEqual(trie.search("word"), True)
        self.assertEqual(trie.search("world"), False)


if __name__ == "__main__":
    ut.main()
