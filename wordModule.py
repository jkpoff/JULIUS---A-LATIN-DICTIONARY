from wiktionaryparser import WiktionaryParser

# Creates "Word" class using wiktionaryparser to pull dictionary entry for user-searched word
class Word:
    def __init__(self, word):
        parser = WiktionaryParser()
        parser.set_default_language('latin')

        self.word = word
        self.latinWord = parser.fetch(word)

    # Includes functions to grab word definition and etymology
    def getDefinition(self):
        try:
            self.definition = (self.latinWord[0]['definitions'][0]['text'])
            return self.definition
        except IndexError as e:
            return e

    def getEtymology(self):
        self.etymology = (self.latinWord[0]['etymology'])
        return self.etymology

    def getSynonyms(self):
            self.examples = (self.latinWord[0]['definitions'][0]['examples'])
            synonyms = []
            for example in self.examples:
                if "Synonym:" in example:
                    synonyms.append(example) 
                if "Synonyms:" in example:
                    synonyms.append(example) 
            return synonyms