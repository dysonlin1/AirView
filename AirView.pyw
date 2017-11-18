# AirView
# plot air voltage signals from a CSV file
# with Matplotlib and tkinter
#
# 台灣地震預測研究所 所長
# 林湧森
# 2017-11-17 09:52 UTC+8

import pandas as pd
import tkinter as Tk
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
plt.style.use('ggplot')

graph_title = 'AirView 5.0.2 宜蘭站 Yilan Station  空氣2號 Air 2 (Arduino Uno + LF298N)'
csv_file_name = '2017-05-16 AirView.csv'
df = pd.read_csv(csv_file_name, 
                 names=['Time', 'Air Voltage (mV)'], 
                 parse_dates=['Time'])

root = Tk.Tk()
root.title(graph_title)

# 設定圖形尺寸與解析度
f = Figure(figsize=(9, 5), dpi=100)
a = f.add_subplot(111)

# 繪製圖形
a.plot(df['Time'], df['Air Voltage (mV)'], color='black')

# Release memory
#del df
#gc.collect()

# 把繪製的圖形顯示到Tkinter視窗
canvas = FigureCanvasTkAgg(f, master=root)
canvas.show()
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

# 把Matplotlib繪製圖形的工具列顯示到Tkinter視窗
toolbar = NavigationToolbar2TkAgg(canvas, root)
toolbar.update()
canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

Tk.mainloop()
