from trie import Trie

# when you enter a digit prefix it should return the list of words

nums_to_chars = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}


def words_for_num_string(num_str, trie):
    prefixes = []
    find_prefix('', num_str, prefixes)
    return trie.words_for_prefixes(prefixes)


def find_prefix(letters, nums_to_process, prefixes):
    # pudb.set_trace()
    if not nums_to_process:
        prefixes.append(letters)
        return
    num = nums_to_process[0]

    for char in nums_to_chars[num]:
        find_prefix(letters + char, nums_to_process[1:], prefixes)


def main():
    some_trie = Trie(['do', 'dog', 'done'])
    print some_trie.words_for_prefix('do')


if __name__ == '__main__':
    main()
