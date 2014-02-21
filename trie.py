# each node is associated with child nodes.
# each node contains a reference to its parent
# each node contains references to all its children.
# each node contains a letter value except root node


import pudb


class Trie(object):
    def __init__(self, word_list):
        self.root = Node(None)
        for word in word_list:
            self.add_word(word)

    def add_word(self, word):
        temp = self.root
        for char in word:
            for child in temp.children:
                if child.value == char:
                    temp = child
                    break
            else:
                temp = temp.addChild(char)


    def words_for_prefix(self, prefix):
        if not isinstance(prefix, str):
            raise ValueError('Wrong class, dummy!')
        temp = self.root
        for letter in prefix:
            for child in temp.children:
                if child.value == letter:
                    temp = child
                    break
            else:
                return []
        words = []
        self.build_word(temp, prefix, words)
        return words

    def words_for_prefixes(self, prefixes):
        words = []
        for prefix in prefixes:
            words.extend(self.words_for_prefix(prefix))
        return words 

    def build_word(self, node, word_so_far, words):
        if node.children:
            for child in node.children:
                new_word = word_so_far + child.value
                self.build_word(child, new_word, words)
        else:
            words.append(word_so_far)


class Node(object):
    def __init__(self, char, parent=None):
        self.value = char
        self.parent = parent
        self.children = []

    def addChild(self, char):
        childNode = Node(char, self)
        self.children.append(childNode)
        return childNode


def main():
    some_trie = Trie(['dog', 'cat'])
    assert(any(node.value == 'd') for node in some_trie.root.children)
    assert(not any(node.value == 'n') for node in some_trie.root.children)
    assert(some_trie.words_for_prefix('d') == ['dog'])
    assert(some_trie.words_for_prefix('') == ['dog', 'cat'])
    assert(some_trie.words_for_prefix('dog') == ['dog'])


if __name__ == '__main__':
    main()
