import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

#to plot the graph
style.use('ggplot')
#to give the start date and end date
start = dt.datetime(2016, 1, 1)
end = dt.datetime.now()
#to read the data frame
df = web.DataReader("TSLA", 'Yahoo', start, end)
df.reset_index(inplace=True)
df.set_index("Date", inplace=True)
df = df.drop("Symbol", axis=1)
df.to_csv('TSLA.csv')
df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)
#to plot the points
df.plot()
#display
plt.show()
