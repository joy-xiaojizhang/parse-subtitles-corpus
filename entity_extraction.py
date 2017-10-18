import glob, os
from nltk import sent_tokenize, word_tokenize, pos_tag, ne_chunk

def extract_entities(text):
    entities = []
    for sentence in sent_tokenize(text):
        chunks = ne_chunk(pos_tag(word_tokenize(sentence)))
        entities.extend([chunk for chunk in chunks if hasattr(chunk, 'node')])
    return entities

def main():
    source_genre = 'Action'
    target_genre = ''
    '''
    raw_data_dir = '../../data/OpenSubtitles/raw/'
    for raw_file in os.listdir(raw_data_dir):
        if raw_file.startswith(source_genre):
    '''
    f = open('../../data/OpenSubtitles/raw/Action_2-fast-2-furious_raw.txt', 'r+')
    text = f.readlines()
    print(extract_entities(text))

if __name__ == "__main__":
    main()
