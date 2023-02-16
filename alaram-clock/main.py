import time
from playsound import playsound

# set the time for the alarm to go off
alarm_time = input("Enter the time in 'HH:MM:SS AM/PM' format: ")

# convert alarm time to 24-hour format
alarm_time = time.strftime("%H:%M:%S", time.strptime(alarm_time, "%I:%M:%S %p"))

print(f"Alarm set for {alarm_time}")

while True:
    # get the current time
    current_time = time.strftime("%H:%M:%S")

    # check if the current time matches the alarm time
    if current_time == alarm_time:
        print("Wake up!")
        # play an alarm sound
        playsound("path/to/alarm/sound.mp3")
        break

    # wait for 1 second before checking the time again
    time.sleep(1)
