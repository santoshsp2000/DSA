# 211. Design Add and Search Words Data Structure


class Node:
    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = Node()
            node = node.children[i]
        node.is_word = True

    def search(self, word: str) -> bool:
        def is_Found(ind, root):
            if ind == len(word):
                return root.is_word

            if word[ind] == '.':
                for char in root.children:
                    if is_Found(ind + 1, root.children[char]):
                        return True

            elif word[ind] in root.children:
                return is_Found(ind + 1, root.children[word[ind]])
            return False

        return is_Found(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)