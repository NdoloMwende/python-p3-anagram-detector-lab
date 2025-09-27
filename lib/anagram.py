# your code goes here!

# def match(gram,list_cands):
#     anagrams = []
#     for word in list_cands:
#         if sorted(word.lower()) == sorted(gram.lower()):
#             anagrams.append(word)
#     print (anagrams)
# match("Asper",["Apers","Maey","njiku","Spare","Spear", "Saper"])

#  ["Apers","Maey","njiku","Spare","Spear", "Saper"]

class Anagram:
    def __init__(self,word = None):
        if word is not None:
            self._word = word
        else:
            raise ValueError("Enter word")
        
    def match(self,list_cands=["Apers","Maey","njiku","Spare","Spear", "Saper"]):
        anagrams = []
        for cand in list_cands:
            if sorted(cand.lower()) == sorted(self._word.lower()):
                anagrams.append(cand)
        print(anagrams)
        return anagrams

asper = Anagram("Asper")
asper.match()