# Import required libraries
import matplotlib.pyplot as plt
import numpy as np
import random
import time
import serial

# Change ACM1 To AMC0 if needed for trouble shooting
ser = serial.Serial('/dev/ttyACM1', 9600, timeout=1)
ser.flush()

# Initialize empty lists for storing data
time_milli = []
temp = []
pressure = []

# Set up the plot with matplotlib
plt.ion()  # Turn on interactive mode
fig, (ax1, ax2) = plt.subplots(2, 1)  # Create figure and axis objects for two subplots

# Set axis labels and titles
ax1.set_xlabel('Time (ms)')
ax1.set_ylabel('Temperature')
ax1.set_title('Temperature vs. Time')
ax2.set_xlabel('Time (ms)')
ax2.set_ylabel('Pressure')
ax2.set_title('Pressure vs. Time')

# Set up the initial plot with empty data
line1, = ax1.plot(time_milli, temp, 'b-')
line2, = ax2.plot(time_milli, pressure, 'b-')

# Function to update the plot with new data
def update_plot():
    line1.set_data(time_milli, temp)  # Update temperature vs. time plot
    line2.set_data(time_milli, pressure)  # Update pressure vs. time plot
    ax1.relim()  # Update limits for temperature vs. time plot
    ax1.autoscale_view()  # Update limits for temperature vs. time plot
    ax2.relim()  # Update limits for pressure vs. time plot
    ax2.autoscale_view()  # Update limits for pressure vs. time plot
    fig.canvas.draw()  # Redraw the plot

# Main loop to read data from serial port and update plot in real-time
while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        data_list = line.split(',')
        time_milli.append(int(data_list[0]))
        temp.append(int(data_list[1]))
        pressure.append(int(data_list[2]))
        update_plot()  # Update the plot with new data
    time.sleep(0.01)  # Sleep briefly to avoid overloading the serial port

# Turn off interactive mode and display the plot
plt.ioff()
plt.show()
