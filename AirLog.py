# AirLog 2.0.0
# save air voltage signals to a CSV file
#
# 台灣地震預測研究所 所長
# 林湧森
# 2017-11-17 10:56 UTC+8

# Algorithm:
# repeat forever:
# 1. read 128 data from serial port
# 2. average them
# 3. write the average to csv file

import serial
import time

def get_date_stamp():
    date_stamp = time.strftime("%Y-%m-%d")
    return date_stamp

def get_datetime_stamp():
    datetime_stamp = time.strftime("%Y-%m-%d %H:%M:%S")
    return datetime_stamp

port_name = 'COM4'
baud = 9600
timeout = 1
port = None
csv_file = None

try:
    port = serial.Serial(port_name, baud, timeout=timeout)
    if port is None:
        print('Cannot open the serial port.')
        print('Please unplug the USB cable and then reconnect Air 1.') 
    else:
        print(port)
    port.flushInput() # flush serial input buffer, discarding all its contents
    #data_number = 0
    
    # discard firt read: it may be incomplete data
    line = port.readline().decode('utf8')
    print('Discard first read: it may be incomplete data')
    if line is '':
        print('Empty line.')
        air_voltage = float('nan')
    else:
        print(line)
        air_voltage = float(line)

    date_stamp = get_date_stamp()
    #csv_file_name = date_stamp + ' AirView' + '.csv'
    csv_file_name = '2019-11-17 AirView.csv'
    print(csv_file_name)
    print('AirLog will run forever.')
    print('If you want to stop AirLog, select Kernel->Interrupt.')

    with open(csv_file_name, 'a') as csv_file:
        # write an empty data to make Bokeh plot a break point
        datetime_stamp = get_datetime_stamp()
        data = datetime_stamp + ',\n'
        data_number = 0
        # print(str(data_number), data)
        csv_file.write(data)
        csv_file.flush()
        
        while True: # infinite loop: read line from serial port
            buffer_size = 128
            buffer = []
            buffer_sum = 0
            for i in range(buffer_size):
                line = port.readline().decode('utf8')
                if line is '':
                    #print('Empty line.')
                    air_voltage = float('nan')
                else:
                    #print(line)
                    air_voltage = float(line)
                buffer.append(air_voltage)
                buffer_sum += air_voltage
                #datetime_stamp = get_datetime_stamp()
                # print(str(i+1), ':', datetime_stamp, line)
            average_air_voltage = buffer_sum / buffer_size
            datetime_stamp = get_datetime_stamp()
            data = datetime_stamp + ',' + str(average_air_voltage) + '\n'
            data_number += 1
            # print(str(data_number), data)
            csv_file.write(data)
            csv_file.flush()
#except:
    #if port is None:
        #print('Cannot open the serial port.')
        #print('Please unplug the USB cable and then reconnect Air 2.')
finally:
    #csv_file.close()
    if csv_file is not None:
        print('CSV file has been closed:', csv_file.closed)

    if port is not None:
        port.close()
        print(port)