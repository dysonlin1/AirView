# coding: utf-8
# To run AirView, type in a command window: 
# bokeh serve --show AirView.py
import numpy as np
from bokeh.io import curdoc
from bokeh.layouts import row, column, widgetbox
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Slider, TextInput
from bokeh.models import Button
import pandas as pd
from bokeh.plotting import figure, output_file, show, output_notebook
from bokeh.models import DatetimeTickFormatter

graph_title = 'AirView V4.0.7'
csv_file_name = '2017-05-16 AirView.csv'

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

df = pd.read_csv(csv_file_name, names=['Time', 'Air Voltage (mV)'], 
                 parse_dates=['Time'])
r = p.line(df['Time'], df['Air Voltage (mV)'])

ds = r.data_source

# callback for update graph


# refresh graph when Refresh button is pressed
button = Button(label="Refresh")

# put the button and plot in a layout and add to the document 
curdoc().add_root(column(button, p))

curdoc().title = graph_title