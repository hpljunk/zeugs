file_ = open('/home/hpl/pythonzeugs/globalgroove.txt')
#file_ = open('/home/hpl/pythonzeugs/jeeves.txt')

import markovgen

markov = markovgen.Markov(file_)

print markov.generate_markov_text()
