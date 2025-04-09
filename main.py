import time
import UMux_Sensors
import machine
import mqtt
import adc
import Display
import AQI
import Wifi_setup
import os

fs_stat = os.statvfs('/')
total = fs_stat[2] * fs_stat[0]  # Total size
free = fs_stat[3] * fs_stat[0]  # Free space
used = total - free  # Used space

print(f"Total Flash: {total} bytes")
print(f"Used Flash :  {used} bytes")
print(f"Free Flash : {free}  bytes")

mqtt.Beep(.2, 3)

time.sleep(3)

# --------------Test area   -----------------
# -------------------------------------------

Display.Introduction_Pages()

Display.Page_Switch(Display.main_2)
time.sleep(2)

UMux_Sensors.Device_Booting()

mqtt.Start_Thread()

mqtt.Convert_UID_QR()

try:
    while True:
        mqtt.Main_Function_Loop()

except Exception as e:
    print("Main Loop Error:", e)



