from diaries.AbstractDiary import AbstractDiary

class UntenDiary(AbstractDiary):
    def get_date(self):
        return "2023-12-14"
    def get_summary(self):
        return "みかん食べた。みかんアレルギーなの忘れてた。"
    def get_author(self):
        return "Unten"