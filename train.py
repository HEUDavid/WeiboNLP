'''
训练模型
会生成 sentiment.marshal.3 文件
在 /usr/local/lib/python3.6/dist-packages/snownlp-0.12.3-py3.6.egg/snownlp/sentiment/__init__.py 中
修改 data_path 指向新的模型
'''

from snownlp import sentiment


def train():
    sentiment.train('neg.txt', 'pos.txt')
    sentiment.save('sentiment.marshal')


train()
