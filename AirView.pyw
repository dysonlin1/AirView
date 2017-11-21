# AirView
# plot air voltage signals from a CSV file
# with Matplotlib and tkinter
#
# 台灣地震預測研究所 所長
# 林湧森
# 2017-11-17 09:52 UTC+8

import pandas as pd

import matplotlib
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import matplotlib.font_manager as fm

import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

def destroy(e):
    sys.exit()
    

graph_title = 'AirView 5.0.4 宜蘭站 空氣2號 Yilan Station Air 2 (Arduino Uno + LF298N)'
csv_file_name = '2017-05-16 AirView.csv'
df = pd.read_csv(csv_file_name, 
                 names=['Time', 'Air Voltage (mV)'], 
                 parse_dates=['Time'])

root = Tk.Tk()
root.wm_title(graph_title)


# 設定圖形尺寸與解析度
figure = Figure(figsize=(10, 5), dpi=100)
axis1 = figure.add_subplot(111)

# set x and y
x = df['Time']
y = df['Air Voltage (mV)']

# 繪製圖形
axis1.plot(x, y)
#axis1.plot(x, y, color='black')
axis1.set_title(graph_title, fontproperties='SimHei', fontsize=14)
#axis1.set_title(graph_title, fontproperties='SimHei', fontsize=24)
axis1.set_xlabel('時間 Time', fontproperties='SimHei')
axis1.set_ylabel('空氣電壓 Air Voltage (mV)', fontproperties='SimHei')

# Release memory
#del df
#gc.collect()

# 把繪製的圖形顯示到Tkinter視窗
canvas = FigureCanvasTkAgg(figure, master=root)
canvas.show()
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

# 把Matplotlib繪製圖形的工具列顯示到Tkinter視窗
toolbar = NavigationToolbar2TkAgg(canvas, root)
toolbar.update()
canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

Tk.mainloop()
