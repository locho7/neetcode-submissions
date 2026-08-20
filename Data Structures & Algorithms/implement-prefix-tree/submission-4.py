class PrefixTree:

    def __init__(self):
        self.children = {}
        self.isWordEnd = False

    def insert(self, word: str) -> None:
        p = self
        for char in word:
            char = char.lower()
            if char not in p.children:
                p.children[char] = PrefixTree()
            p = p.children[char]
        p.isWordEnd = True

    def search(self, word: str) -> bool:
        p = self
        for char in word:
            char = char.lower()
            if char not in p.children:
                return False
            p = p.children[char]
        return p.isWordEnd

    def startsWith(self, prefix: str) -> bool:
        p = self
        for char in prefix:
            char = char.lower()
            if char not in p.children:
                return False
            p = p.children[char]
        return True
        