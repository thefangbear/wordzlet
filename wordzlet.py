
import _settings
import dict
from ireport import report
import _settings
"""
report("initialising dict from wordzleet")
d = dict.Dictionary()
report("opening file at " + _settings.READ_FILE_PATH)
with open(_settings.READ_FILE_PATH) as fd:
    file = fd.readlines()

report("Parsing file into Set")
words = [word.strip().strip('\t').strip('\n').lower() for word in file]
report(words)
s = dict.SetInput(file, d)

print(s.word_pair)
report("\n\n\n")
print(s.words)
report("\n\n\n")
print(s.definitions)


"""

import qapi

q = qapi.QuizletAPI()
q.create_set("testSet001", ["milk", "asdfkjb", "lollol"], "en", ["honey", "123123", -133], "en")