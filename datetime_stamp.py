# -*- coding: utf-8 -*-
# datetime_stamp.py
import time

def get_date_stamp():
    date_stamp = time.strftime("%Y-%m-%d")
    return date_stamp

def get_datetime_stamp():
    datetime_stamp = time.strftime("%Y-%m-%d-%H-%M-%S")
    return datetime_stamp