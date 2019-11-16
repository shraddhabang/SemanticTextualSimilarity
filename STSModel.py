import sys

from nltk import pos_tag
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize


class CorpusReader:

    def __init__(self):
        self.data = []

    def read_data(self, input_file):
        with open(input_file, 'r', encoding='utf8') as data:
            lines = data.read().splitlines()
        for line in lines:
            self.data.append(line.split("\t"))

    def tokenise(self, sentence):
        return (word_tokenize(sentence))

    def lematize(self, sentence):
        tokenised_words = self.tokenise(sentence)
        lemmatizer = WordNetLemmatizer()
        res = []
        tagged_word = pos_tag(tokenised_words)
        tag_dict = {"J": wordnet.ADJ,
                    "N": wordnet.NOUN,
                    "V": wordnet.VERB,
                    "R": wordnet.ADV}
        for i in range(len(tokenised_words)):
            res.append(
                lemmatizer.lemmatize(tagged_word[i][0], tag_dict.get(tagged_word[i][1][0].upper(), wordnet.NOUN)))
        return res

    def pos_tagging(self, sentence, is_sentence=False):
        if is_sentence:
            return pos_tag(self.tokenise(sentence))
        else:
            return pos_tag(sentence)

    def sentence_length(self, sentence):
        return len(self.tokenise(sentence))

    def wordnet_features(self):
        pass

    def parse_tree(self):
        pass


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please provide the input file only")
        exit(0)
    input_file = sys.argv[1]
    reader = CorpusReader()
    reader.read_data(input_file)
    # print(reader.data)
    while True:
        print("Choose from the following options:")
        print("1. Tokenize sentence")
        print("2. Lemmatize sentence")
        print("3. Find POS tag")
        print("4. Get Parse tree")
        print("5. Get wordnet features")
        print("6. Length of sentence")
        print("7. Continue with model")
        option = int(input("Option? "))
        if option in range(0, 7):
            sentence = input("Please enter the sentence ")
            if option == 1:
                print(reader.tokenise(sentence))
            elif option == 2:
                print(reader.lematize(sentence))
            elif option == 3:
                print(reader.pos_tagging(sentence, True))
            elif option == 4:
                print(reader.parse_tree())
            elif option == 5:
                print(reader.wordnet_features())
            elif option == 6:
                print(reader.sentence_length(sentence))
            else:
                exit(0)
        else:
            print("Please select the correct option")