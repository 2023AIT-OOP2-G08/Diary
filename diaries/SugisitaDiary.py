from diaries.AbstractDiary import AbstractDiary

class SugisitaDiary(AbstractDiary):
    def get_date(self):
        return "2021-12-14"
    def get_summary(self):
        return "シュークリーム食べた"
    def get_author(self):
        return "Sugisita"