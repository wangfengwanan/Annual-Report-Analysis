from jieba import analyse
import os

input_dir = '../data/annual_report_part'
output_dir = '../output/annual_report_keywords/'

if not os.path.exists(output_dir):
    os.mkdir(output_dir)

def extract_keywords(data):
    keywords = analyse.extract_tags(data, topK=200)
    return keywords

def get_keywords(input_dir, output_dir):
    for (parent, _, filenames) in os.walk(input_dir):
            for filename in filenames:
                input_path  = parent + '/' + filename
                output_path = output_dir + filename
                with open(input_path, 'r', encoding='utf-8') as fr:
                    words = fr.readlines()
                    keywords = extract_keywords(words[0])
                with open(output_path, 'w', encoding='utf-8') as fw:
                    for keyword in keywords:
                        fw.write(keyword + ' ')

if __name__ == '__main__':
    get_keywords(input_dir, output_dir)


