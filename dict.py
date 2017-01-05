
import requests
import json
import _settings
from ireport import report


class SetInput(object):

    def __init__(self, words, dictionary):
        report('Set initializer called. Initializing set...')
        self.words = words
        self.definitions = []
        self.word_pair = {}
        for word in words:
            word = word.strip('\n')
            definition = dictionary.get_word(word)
            self.word_pair[word] = definition
            self.definitions.append(definition)

    def alter_definition(self, word, definition):
        try:
            self.word_pair[word] = definition
        except KeyError:
            report("Fatal error: word not found:" + word + " - " + definition)


class Dictionary(object):

    def __init__(self):
        report("dictionary instance called. Loading dict...")
        self.definitions = json.loads(requests.get(_settings.JSON_DICT_PATH, stream=True).text.lower())
        report("successfully loaded dictionary!")

    def get_word(self, word):
        try:
            meaning = self.definitions[word]
            report("Word " + word + " meaning found. Meaning: " + meaning)
            return meaning
        except KeyError:
            report("Fatal error: no such word as " + word)
            return -1

    def set_word(self, word, meaning):
        self.definitions[word] = meaning