# coding: utf-8
# To run AirView, type in a command window: 
# bokeh serve --show AirView.py
import numpy as np
from bokeh.io import curdoc
from bokeh.layouts import row, column, widgetbox
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Slider, TextInput
import pandas as pd
from bokeh.plotting import figure, output_file, show, output_notebook
from bokeh.models import DatetimeTickFormatter

graph_title = 'AirView V4.0.7'
csv_file_name = '2017-05-16 AirView.csv'
df = pd.read_csv(csv_file_name, names=['Time', 'Air Voltage (mV)'], 
                 parse_dates=['Time'])

p = figure(plot_width=900, plot_height=500, x_axis_type="datetime",
        title=graph_title, 
        x_axis_label='Time', y_axis_label='Air Voltage (mV)')

p.xaxis[0].formatter = DatetimeTickFormatter(
        years = '%Y',
        months = '%Y-%m',
        days = '%Y-%m-%d',
        hours = '%H:%M:%S',
        hourmin = '%H:%M:%S',
        minutes = '%H:%M:%S',
        minsec = '%H:%M:%S',
        seconds = '%H:%M:%S',
        milliseconds = '%H:%M:%S',
        microseconds = '%H:%M:%S'
        )

p.line(df['Time'], df['Air Voltage (mV)'])






    
curdoc().add_root(p)
curdoc().title = graph_title