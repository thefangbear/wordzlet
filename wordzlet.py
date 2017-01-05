
# coding: utf-8

import dict
from ireport import report
import _settings
import qapi

report("initialising dict from wordzleet")
d = dict.Dictionary()
report("opening file at " + _settings.READ_FILE_PATH)
with open(_settings.READ_FILE_PATH) as fd:
    file = fd.readlines()

report("Parsing file into Set")
words = [word.strip().strip('\t').strip('\n').lower() for word in file]
report(words)
s = dict.SetInput(file, d)


q = qapi.QuizletAPI()
q.create_set("TestMerriamVocabInput", s.words, "en", s.definitions, "en")
