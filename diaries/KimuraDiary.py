from diaries.AbstractDiary import AbstractDiary

class KimuraDiary(AbstractDiary):
    def get_date(self):
        return "2023-12-14"
    def get_summary(self):
        return "鍋作った。材料切って煮るだけなの楽でいい。"
    def get_author(self):
        return "Kimura"