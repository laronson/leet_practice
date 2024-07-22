class TrieNode:
  def __init__(self, val):
    self.nodes = [None]*26
    self.val = val
    self.isWord = False

class PrefixTree:

    def __init__(self):
      self.root = TrieNode(None)
        

    def insert(self, word: str) -> None:
      curr = self.root
      word.lower()
      for c in word:
        nextNode = curr.nodes[(ord(c) - ord('a'))]
        
        if not nextNode:
          curr.nodes[(ord(c) - ord('a'))] = TrieNode(c)
          curr = curr.nodes[(ord(c) - ord('a'))]
          continue
        else:
          curr = nextNode

      curr.isWord=True

    def search(self, word: str) -> bool:
      wordNode = self.getWord(word)
      return wordNode.isWord
        

    def startsWith(self, prefix: str) -> bool:      
      return True if self.getWord(prefix) else False
    
    def getWord(self, word):
      curr = self.root
      word.lower()
      for c in word:
        nextNode = curr.nodes[(ord(c) - ord('a'))]
        if not nextNode:
          return False
        else:
          curr = nextNode
      return curr
        
        