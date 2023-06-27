import keyboard
import time
import os
from datetime import datetime
from openpyxl import Workbook

current_directory = os.getcwd()
print("Current working directory:", current_directory)

# Global timer variables
global_timer_running = False
global_timer_start = 0
global_timer_end = 0

# Individual timer variables
timers = {'w': [], 'a': [], 's': [], 'd': []}
key_press_count = {timer: 0 for timer in timers.keys()}

# Create Excel workbook and sheet
wb = Workbook()
ws = wb.active
ws.append(['Beginning', 'End', 'Timer', 'Duration'])

def toggle_timer(timer):
    if global_timer_running:
        if timer not in timers:
            print(f'Invalid timer "{timer}"')
            return

        if timer in timers and timers[timer]:
            # Stop the timer if it is already running
            timers[timer].append(time.time() - global_timer_start)
            print(f'Timer {timer.upper()} stopped at {timers[timer][-1]} seconds.')
        else:
            timers[timer].append(time.time() - global_timer_start)
            print(f'Timer {timer.upper()} started at {timers[timer][-1]} seconds.')
    else:
        print('Global timer is not running. Start the global timer (press "i") before using individual timers.')

def on_key_press(event):
    global global_timer_running, global_timer_start, global_timer_end

    if event.name == 'i':
        if not global_timer_running:
            global_timer_start = time.time()
            global_timer_running = True
            print('Global timer started.')
        else:
            print('Global timer is already running.')

    elif event.name in timers.keys():
        toggle_timer(event.name)
        key_press_count[event.name] += 1

    if event.name == 'space':
        if global_timer_running and not keyboard.is_pressed('i'):
            global_timer_end = time.time() - global_timer_start
            global_timer_running = False
            print('Global timer stopped.')

            # Generate filename with the format "yyyymmdd-contaje-hh:mm.xlsx"
            current_datetime = datetime.now().strftime('%Y_%m_%d-%H_%M')
            filename = f'{current_datetime}-contaje.xlsx'

            # Save the .xlsx file to the current working directory
            filepath = os.path.join(current_directory, filename)

            # Write timer data to Excel file
            rows = []
            for timer, timestamps in timers.items():
                for i in range(0, len(timestamps), 2):
                    start_time = timestamps[i]
                    end_time = timestamps[i+1] if i+1 < len(timestamps) else global_timer_end
                    duration = end_time - start_time
                    rows.append([start_time, end_time, timer.upper(), duration])

            # Sort rows based on the 'Beginning' column in ascending order
            rows.sort(key=lambda x: x[0])

            for row in rows:
                ws.append(row)

            wb.save(filepath)
            print('Timer data saved to', filepath)

            # Calculate the total duration of each timer
            total_durations = {timer: sum([row[3] for row in ws.iter_rows(values_only=True) if row[2] == timer.upper()]) for timer in timers.keys()}
            total_global_duration = global_timer_end if global_timer_running else 0
            print('Total Durations:')
            for timer, duration in total_durations.items():
                print(f'{timer.upper()}: {duration} seconds')

            # Calculate the frequency of each timer
            print('Frequency:')
            for timer, count in key_press_count.items():
                if timer != 'global':
                    print(f'{timer.upper()}: {count} times')

            print(f'Global: {total_global_duration} seconds')

keyboard.on_press(on_key_press)

print('Press letter i to start the global timer.')
print('Press space to stop the global timer and save timer data.')
print('Press w, a, s, or d to toggle individual timers.')

keyboard.wait()
