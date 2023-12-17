from diaries.DiarySample import DiarySample
from diaries.UntenDiary import UntenDiary
from diaries.OdagiriDiary import OdagiriDiary
from diaries.ShimizuDialy import ShimizuDiary
from diaries.KimuraDiary import KimuraDiary
from diaries.TsugeDiary import TsugeDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    OdagiriDiary(),
    ShimizuDiary(),
    UntenDiary(),
    KimuraDiary(),
    TsugeDiary(),
    ]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()