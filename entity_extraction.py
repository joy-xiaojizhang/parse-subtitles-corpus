import nltk, glob, os

def extract_entity_names(t):
    entity_names = []

    if hasattr(t, 'label') and t.label:
        if t.label() == 'NE':
            entity_names.append(' '.join([child[0] for child in t]))
        else:
            for child in t:
                entity_names.extend(extract_entity_names(child))

    return entity_names

source_genre = 'Action'
raw_data_dir = '../../data/OpenSubtitles/raw_capitalized/'

with open('entities.txt', 'w') as entities_file:
    for raw_file in os.listdir(raw_data_dir):
        if raw_file.startswith(source_genre):
            print('Start processing: ' + raw_file)
            all_entities = set()
            entities_file.write('++++' + raw_file + '++++\n')
            with open(raw_data_dir + raw_file, 'r') as f:
                for line in f:
                    sentences = nltk.sent_tokenize(line)
                    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
                    tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
                    chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=True)

                    entities = []
                    for tree in chunked_sentences:
                        entities.extend(extract_entity_names(tree))

                    all_entities.update(entities) 
                entities_file.write(','.join(all_entities) + '\n')
            print('Processing finished: ' + raw_file)
