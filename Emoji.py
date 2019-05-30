# 表情统计
import re
from collections import Counter


class Emoji:
    def __init__(self, text_list):
        self.text_list = text_list
        self.emoji_list = []
        self.emoji_dict = {}
        self.count()

    def count(self):
        for text in self.text_list:
            # emojis = re.findall(re.compile(r'(\[.*?\])', re.S), text)  # 微博表情
            emojis = re.findall(re.compile(
                r'[\U00010000-\U0010ffff]', re.S), text)  # 输入法表情

            if emojis:
                for emoji in emojis:
                    self.emoji_list.append(emoji)
        self.emoji_dict = Counter(self.emoji_list)


list = ['华为手机，👎传感器是个垃圾👎',
        '还特么打不出去电话👎，信号弱爆了👎，',
        '草泥马华为，还搞饥饿营销😡，早晚得饿死😂以后再也不买国产机😡，国产机吃屎吧！😂']
e = Emoji(list)
print(e.emoji_dict)
