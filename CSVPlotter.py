import matplotlib.pyplot as plt
import numpy as np
import csv
import seaborn as sns
import datetime

# Load data from the .csv file
time, temp, pressure = [], [], []
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the title row
    next(reader)  # Skip the Header row
    for row in reader:
        time.append(float(row[0]))
        temp.append(float(row[1]))
        pressure.append(float(row[2]))

plt.ion()  # Turn on interactive mode
fig, (ax1, ax2) = plt.subplots(2, 1)  # Create figure and axis objects for two subplots

# Set axis labels and titles
ax1.set_xlabel('Time (ms)')
ax1.set_ylabel('Temperature')
ax1.set_title("Date/Time:" + datetime.now + "Temperature vs. Time")
ax2.set_xlabel('Time (ms)')
ax2.set_ylabel('Pressure')
ax2.set_title('Pressure vs. Time')

# Set up the initial plot with empty data
line1, = ax1.plot(time, temp, 'b-')
line2, = ax2.plot(time, pressure, 'b-')
