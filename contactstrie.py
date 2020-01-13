class TrieNode: 

    def __init__(self): 
        self.children = [None] * 26
        self.end = False
        self.size = 0

class Trie: 
      
    def __init__(self): 
        self.root = self.getNode() 
  
    def getNode(self): 
        return TrieNode() 
  
    def _charToIndex(self, ch):           
        return ord(ch) - ord('a') 

    def add(self, key):           
        crawl = self.root 
        for c in key: 
            index = self._charToIndex(c) 
            if not crawl.children[index]: 
                crawl.children[index] = self.getNode() 
            crawl = crawl.children[index] 
            crawl.size += 1
        crawl.end = True
  
    def find(self, key):           
        crawl = self.root 
        for c in key: 
            index = self._charToIndex(c) 
            if not crawl.children[index]: 
                return 0
            crawl = crawl.children[index]
        return crawl.size

def contacts(queries):
    trie = Trie()
    results = []
    for q in queries:
        c, v = q[0], q[1]
        if c == "add":
           trie.add(v)
        elif c == "find":
            results.append(trie.find(v))
    return results

trie = Trie()

trie.add("hack")
trie.add("hackerrank")

print(trie.find("hac"))
print(trie.find("hak"))