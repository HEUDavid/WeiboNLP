# 文本预处理
import pandas as pd
from snownlp import SnowNLP


def select(path):
    '''
    用旧模型把文件中情感倾向比较极端的文本挑选出来作为训练的样本
    '''
    names = ['博主主页', '博主昵称', '发布时间', '微博内容', '微博地址', '微博来源', '评论', '赞', '转发']
    data = pd.read_csv(path, header=None, names=names, usecols=['微博内容'])

    pos_list = []
    neg_list = []

    for text in data['微博内容']:
        if isPos(text):
            pos_list.append(text + '\n')
        if isNeg(text):
            neg_list.append(text + '\n')

    print('pos:', len(pos_list))
    print('neg:', len(neg_list))

    with open('pos.txt', 'a+') as f:
        f.writelines(pos_list)
    with open('neg.txt', 'a+') as f:
        f.writelines(neg_list)


def isPos(text):
    if not text:
        return False
    s = SnowNLP(text)
    if s.sentiments > 0.95:
        return True
    else:
        return False


def isNeg(text):
    if not text:
        return False
    s = SnowNLP(text)
    if s.sentiments < 0.15:
        return True
    else:
        return False


def main():
    path = './data/华为.csv'
    select(path)


main()
