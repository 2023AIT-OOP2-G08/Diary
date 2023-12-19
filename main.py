
from diaries.TatsunoDiary import TatsunoDiary
# ↓のリストには、メンバーの各日記が格納されます。
diaries = [TatsunoDiary(),]#変更箇所
for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()