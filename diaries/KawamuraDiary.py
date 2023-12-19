from diaries.AbstractDiary import AbstractDiary

class KawamuraDiary(AbstractDiary):
    def get_date(self):
        return "2023-12-19"
    def get_summary(self):
        return """寝て起きたら丸１日過ぎていた。
最近多いのでいい加減病院行った方が良い気がする..."""

    def get_author(self):
        return "Kawamura"