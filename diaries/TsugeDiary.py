from diaries.AbstractDiary import AbstractDiary

class TsugeDiary(AbstractDiary):
    def get_date(self):
        return "2023-12-14"
    def get_summary(self):
        return """今日は焼肉だ！！"""
    def get_author(self):
            return "Tsuge"
