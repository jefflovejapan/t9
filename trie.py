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
        for i in xrange(len(word)):
            for child in temp.children:
                if child.value == word[i]:
                    temp = child
                    if i == len(word) - 1:
                        print 'i got created'
                        child.add_child('')
                    break

            else:
                temp = temp.add_child(word[i])

                # Needs to be in both locations so it gets hit regardless
                # of sorting
                if i == len(word) - 1:
                    print ('i got created down below')
                    temp.add_child('')

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

    def add_child(self, char):
        childNode = Node(char, self)
        self.children.append(childNode)
        return childNode
