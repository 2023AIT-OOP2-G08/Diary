from diaries.AbstractDiary import AbstractDiary


class ShimizuDiary(AbstractDiary):
    def get_date(self):
        return "2021-12-14"

    def get_summary(self):
        return """カレー美味しかった"""

    def get_author(self):
        return "Shimizu"
