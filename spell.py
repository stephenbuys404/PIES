#autocorrect
from autocorrect import Speller

spell = Speller(lang='en')
print(spell('caak'))
print(spell('worrd'))
print(spell('forever'))
