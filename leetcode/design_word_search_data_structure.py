'''
This question asks us to create a word search storage class that can store words and then perform searches within the 
word search store to check if a word has been stored.  The class implements two methods: add which adds a word to the 
word store and search which searches for a word in the word store.  When searching for a word, the searching word 
parameter can contain ‘.’ chacacters which act as wildcard characters and can represent any letter.  For example, 
if the word “bay” exists in the word store and the user searches for “.ay” then the method would return true that a word 
exists in the word store that matches the search.

To do this, we must first think about how we want to store our words.  Because we are storing multiple words and we want 
to give users the opportunity to search for those words, a Trie datastructure would make the most sense.  This is 
because Tries can be used to make for easy searching across a wide list of words due to its ability to perform 
prefix-searches of words.

For the add function, we will traverse through our Trie, searching to see if a prefix for the word we are trying to add 
already exists.  If the prefix does, we can set the isEnd variable of that node in the trie to be True to indicate that 
it is the end of a word.  If we do not reach the end of the word we are trying to add in the initial prefix search, we 
will add new nodes to the trie for each nonexistant character until all letters from the new word are added.

For the search function, we will perform a recursive DFS search of the trie to search for a word that exists in the trie 
that matches the search.  The reason why we need to do a recursive DFS search is because if we hit a wildcard character 
in our search word, we will need to backtrack though each node at that point in the Trie to check if a word exists from 
that point that matches the remaining characters in the search word.  If we hit a . character, we iterate through all 
trie nodes in the trie at that point and traverse through each letter path to see if a matches word exists for each
path.  If it does, we return true.  When we hit any other char that is not a ., we can simply navigate to that letter in 
the current trie node, check if it exists, and then continue our traversal. If the node does not exist at that point, we 
can return false.
'''

'''
edge=>[bay,kay,rack] search(ba.)->bay search(.ay) -> bay or kay

1. How do we want to store words and what data structure do we want to use
 - Trie
 - each trie node is going to store an array of len(26) to represent each letter in the alphabet
 that point to other trie nodes if they exist.  Each trie node will also have an isEnd
2. How do we search our data structure for words 
 - backtracking dfs recursive seach of our trie tracing each letter in the searched word down into
 our trie,
3. How do we search our data structure for words with wildcard characters (.)
 - If we hit a . character, trace through each child trie node at the current node and continue search
 down trie for rest of word.  If exists, return first found word.  

1. Create trie node class
2. init wordDictionary class with an empty trie
3. Implement add word method
  3a. Trace through existing trie for existing letter path that matches word.
    3ab. If we hit a point in our trace that a chacacter in word does not exist, start to
    new trie nodes for the remainder of word
  3b. set the trie node that represents the last letter in word to have isEnd = true
4. implement seach
  4a. trace through search word letter by letter searching for a letter path in trie that 
  matches word
  4b.  If we hit a . character, traverse through all trie nodes at that letter starting at 0
  4c. If a trie not exists in this traversal, trace the remainder of the trie for a letter path
  that exists for the remainder of word
    4ca. If no letter path exists that matches word, traverse through the remaining nodes in the root
    trie where . character was found for other nodes and perform traverses there.
  4d. If at the end of the word seach, we hit a node that has isEnd == true, then the word exists

'''
class TrieNode:
  def __init__(self, isEnd):
    #print("AWEFa")
    self.letters = [False] * 26
    self.isEnd = isEnd

class WordDictionary:
  def __init__(self):
    self.root = TrieNode(None)
      

  def addWord(self, word: str) -> None:
    idx, curr = 0, self.root
    while idx < len(word):
      if not curr.letters[ord(word[idx]) - ord('a')]:
        curr.letters[ord(word[idx]) - ord('a')] = TrieNode(None)
      curr = curr.letters[ord(word[idx]) - ord('a')]
        
      idx+=1

    curr.isEnd=True

  def search(self, word: str) -> bool:
    exists = [False]

    def dfs(i,root):
      if not root or exists[0]:
        return
      if i == len(word):
        print(root.isEnd)
        exists[0] = root.isEnd or False
        return
      
      print(word[i])
      if word[i] == '.':
        for c_idx in range(26):
          if root.letters[c_idx]:
            dfs(i+1, root.letters[c_idx])
      else:
        next_node = root.letters[ord(word[i]) - ord('a')]
        dfs(i+1, root.letters[ord(word[i]) - ord('a')])

    dfs(0,self.root)
    return exists[0]
        
