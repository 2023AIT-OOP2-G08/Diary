from diaries.DiarySample import DiarySample
from diaries.UntenDiary import UntenDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(),UntenDiary() ]#変更箇所

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()