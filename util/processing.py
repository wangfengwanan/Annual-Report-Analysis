import jieba
import os, re
import numpy

stop_words_path = 'stop_words.txt'
annual_report_path = '../data/annual_report_all/'
output_file = '../output/all_content_clean.txt'

# 读取停用词表
def read_stop_words(stop_words_path):
    with open(stop_words_path, 'r') as fp:
        stop_words_list = []
        for stop_word in fp.readlines():
            stop_words_list.append(stop_word.strip())
    return stop_words_list

# 分词
def tokenize_word(input_file_path):
    with open(input_file_path, encoding='utf-8') as fp:
        content = ''.join(fp.readlines()).replace('\n','')
        content = re.sub(r"[a-zA-Z0-9]", " ", content)
        content = ' '.join(jieba.cut(content)).split(' ')
    return content

# 去停用词
def drop_stop_words(contents,stop_words):
    contents_clean = []
    for word in contents:
        if len(word) > 1:
            if word in stop_words:
                continue
            contents_clean.append(word)
    return contents_clean

def main():
    all_content_clean = ''
    for (parent,dirnames,filenames) in os.walk(annual_report_path):
        for filename in filenames:
            path  = parent + '/' + filename
            print(path)
            stop_words = read_stop_words(stop_words_path)
            content = tokenize_word(path)
            content_clean = drop_stop_words(content, stop_words)
            content_clean = ' '.join(content_clean)
            all_content_clean = all_content_clean + content_clean + '\n'
    with open(output_file, 'w', encoding='utf-8') as fr:
        fr.write(all_content_clean)

if __name__ == '__main__':
    main()
# print(os.listdir(annual_report_path))