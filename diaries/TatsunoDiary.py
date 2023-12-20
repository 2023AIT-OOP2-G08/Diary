from diaries.AbstractDiary import AbstractDiary

class TatsunoDiary(AbstractDiary):
    def get_date(self):
        return "2021-12-19"
    def get_summary(self):
        return """朝からずっとアニメを観ていた。時間を忘れてしまうほど、面白かった。"""
    def get_author(self):
        return "Tatsuno"
