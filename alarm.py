from datetime import datetime
import time
import winsound

alarm_hour = int(input("Enter alarm hour (0-23): "))
alarm_minute = int(input("Enter alarm minute (0-59): "))

print("Alarm is set!")

while True:
    now = datetime.now()

    if now.hour == alarm_hour and now.minute == alarm_minute:
        print("⏰ Alarm Ringing!")
        winsound.Beep(1000, 3000)
        break

    time.sleep(1)