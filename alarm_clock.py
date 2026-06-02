from datetime import datetime
import time
import winsound

alarm_time = input("Set Alarm (HH:MM:SS): ")

while True:
    now = datetime.now().strftime("%H:%M:%S")
    print("Current Time:", now)

    if now == alarm_time:
        print("⏰ Alarm Ringing!")
        winsound.Beep(1500, 5000)
        break

    time.sleep(1)