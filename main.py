from diaries.DiarySample import DiarySample
from diaries.OdagiriDaiary import OdagiriDiary
from diaries.ShimizuDialy import ShimizuDiary


# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    OdagiriDiary(),
    ShimizuDiary(),
]  # 変更箇所

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
