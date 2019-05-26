# 表情统计
import re
from collections import Counter


class Emoji:
    def __init__(self, text_list):
        self.text_list = text_list
        self.emoji_list = []
        self.emoji_dict = {}

    def count(self):
        for text in self.text_list:
            emojis = re.findall(re.compile(r'(\[.*?\])', re.S), text)
            if emojis:
                for emoji in emojis:
                    self.emoji_list.append(emoji)
        self.emoji_dict = Counter(self.emoji_list)
