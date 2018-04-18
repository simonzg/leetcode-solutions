import datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

progress = {
  '3/24': 10,
  '3/25': 11,
  '3/26': 11,
  '3/27': 2,
  '3/28': 4,
  '3/29': 3,
  '4/1': 10,
  '4/2': 2,
  '4/3': 4,
  '4/4': 3,
  '4/5': 5,
  '4/8': 8,
  '4/11': 2
}

dates = []
counts = []

start = datetime.date(2018,3,24)
d = start

while d <= datetime.date.today():
  month = d.strftime('%m').lstrip('0')
  date = d.strftime('%d').lstrip('0')
  key = month+'/'+date

  dates.append(d)
  if key in progress:
    counts.append(progress[key])
  else:
    counts.append(0)
  d += datetime.timedelta(days=1)

ds = pd.date_range(start=start.strftime('%Y/%m/%d'), end=datetime.date.today().strftime("%Y/%m/%d"))
s = pd.Series(counts, index=dates)

m = pd.rolling_mean(s, 3)
df = pd.DataFrame(s, m)
ax = s.plot(kind='bar', colormap='Accent')
for p in ax.patches:
  ax.annotate(str(int(p.get_height())), (p.get_x()+p.get_width()/2., p.get_height()), ha='center', va='center', xytext=(0, 10), textcoords='offset points')
# m.plot(ax=ax)
# df.plot()
plt.show()
