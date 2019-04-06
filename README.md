# Annual-Report-Analysis

项目目标：

  通过对每个公司发布的年报的相似度进行分析，找出与某公司最相近的其他公司，以便于重点关注其公司业务，对提升公司的竞争力有很大帮助。
  
代码分析：

  util文件夹：
  
    processing.py:
    
    是预处理模块，主要是针对年报进行清洗，并去除停用词，分词，并将所有年报的分词结果保存在output文件夹里（结果太大，不便上传）
    
    stop_words.txt:
    
    停用词表
    
  production文件夹：
  
    word_embeding.py:
    
    对所有年报的分词结果进行词嵌入，使用的是skip-gram模型。
    
    extract_keywords.py：
    
    使用tf-idf提取每份年报的关键词（200个），并将这些关键词对应的向量相加，形成每份年报的向量。
    
    calculate_similarity.py：
    
    分别计算每个公司所对应的年报的余弦相似度。
    
    
