#resource: https://github.com/csurfer/rake-nltk

from rake_nltk import Rake
text = open('../../data/OpenSubtitles/raw/Action_2-fast-2-furious_raw.txt', 'r').read()

r = Rake() # Uses stopwords for english from NLTK, and all puntuation characters.

# If you want to provide your own set of stop words and punctuations to
# r = Rake(<list of stopwords>, <string of puntuations to ignore>)

r.extract_keywords_from_text(text)

# print r.get_ranked_pharases
print(r.get_ranked_phrases_with_scores()) # To get keyword phrases ranked highest to lowest.
