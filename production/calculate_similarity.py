from gensim.models import Word2Vec
import numpy as np
import os

wordVec_size = 150
input_dir = '../output/annual_report_keywords/'
model_path = '../output/word_embeding_150'

num = len(os.listdir(input_dir))
model = Word2Vec.load(model_path)

# 计算每篇年报向量
def calculate_vector(input_path):
    wordVec_per_annual_report = np.zeros(wordVec_size, dtype=float)
    with open(input_path, encoding='utf-8') as fr:
        keywords = fr.readlines()
        for keyword in keywords:
            if model.__contains__(keyword):
                wordVec_per_annual_report += model[keyword]
    return wordVec_per_annual_report

def generate_vector_mat(input_dir):
    wordVec_all = np.zeros([num, wordVec_size], dtype=float)
    row = 0
    for path in os.listdir(input_dir):
        input_path = input_dir + path
        wordVec_per_annual_report = calculate_vector(input_path)
        wordVec_all[row] += wordVec_per_annual_report
        row += 1
    return wordVec_all

def calculate_similarity(wordVec_all):
    vector_list = []
    length = len(wordVec_all)
    for i in range(length):
        vector_1_mod = np.sqrt(wordVec_all[i].dot(wordVec_all[i]))
        for j in range(i, length):
            vector_2_mod = np.sqrt(wordVec_all[j].dot(wordVec_all[j]))
            if vector_1_mod != 0 and vector_2_mod != 0:
                simlarity = (wordVec_all[i].dot(wordVec_all[j])) / (vector_1_mod * vector_2_mod)
            else:
                simlarity = 0
            vector_list.append(simlarity)
    return vector_list

if __name__ == '__main__':
    wordVec_all = generate_vector_mat(input_dir)
    vector_list = calculate_similarity(wordVec_all)