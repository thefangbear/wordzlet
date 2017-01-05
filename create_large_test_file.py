import dict

d = dict.Dictionary()
words = list(d.definitions.keys())
words_new = [word + '\n' for word in words]
with open(".dynamicCache/merriam-webster-all.txt", "w") as fd:
    fd.writelines(words_new)
