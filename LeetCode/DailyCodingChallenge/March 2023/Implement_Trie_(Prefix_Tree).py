# 208. Implement Trie (Prefix Tree)


class Node:
    def __init__(self):
        self.data = {}
        self.is_word = False


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:

        ref = self.root
        for i in word:
            if i not in ref.data:
                ref.data[i] = Node()
            ref = ref.data[i]
        ref.is_word = True

    def search(self, word: str) -> bool:
        ref = self.root
        for i in word:
            if i in ref.data:
                ref = ref.data[i]
            else:
                return False
        else:
            return ref.is_word

    def startsWith(self, prefix: str) -> bool:

        ref = self.root
        for i in prefix:
            print(ref.data)
            if i in ref.data:
                ref = ref.data[i]
            else:
                return False
        else:
            return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
