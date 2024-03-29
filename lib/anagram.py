# your code goes here!

class Anagram:
    
    def __init__(self, wordToCheck):
        self.wordToCheck = wordToCheck
        
    
    @property
    def wordToCheck(self):
        return self._wordToCheck
    
    @wordToCheck.setter
    def wordToCheck(self, word):
        self._wordToCheck = word
    
    def match(self, arr):
        return [word for word in arr if all(char in word for char in self._wordToCheck)] if len(arr) > 0 else []


if __name__ == "__main__":
    listen = Anagram("listen")
    # print(listen.wordToCheck)
    listen.match(['enlists', 'google', 'inlets', 'banana', 'listen'])