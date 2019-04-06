from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import time

output_file = '../output/all_content_clean.txt'

t0 = int(time.time())
with open(output_file, encoding='utf-8') as fp:
    sentences = LineSentence(fp)
    model = Word2Vec(sentences, sg=1, size=150, window=5, min_count=5, workers=-1)
    print('训练耗时 %d s' % (int(time.time()) - t0))
    model.save('../output/word_embeding_150')