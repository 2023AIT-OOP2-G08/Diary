from diaries.DiarySample import DiarySample
from diaries.UntenDiary import UntenDiary
from diaries.OdagiriDiary import OdagiriDiary
from diaries.ShimizuDialy import ShimizuDiary
from diaries.KimuraDiary import KimuraDiary
from diaries.k22089Diary import k22089Diary
from diaries.SugisitaDiary import SugisitaDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    OdagiriDiary(),
    ShimizuDiary(),
    UntenDiary(),
    KimuraDiary(),
    k22089Diary(),
    SugisitaDiary(),
    ]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()