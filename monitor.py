import threading
import datetime
import psutil
import time
import os
import csv


file_path = f"data/{int(time.time())}_plug_times.csv"
timer_start_time = None
timer_running = False


def convert_unix_time(timestamp):
    dt = datetime.datetime.fromtimestamp(timestamp)
    formatted_time = dt.strftime("%I:%M:%S %p, %B %d, %Y")
    return formatted_time


def record_plug_times():
    global timer_start_time, timer_running

    plugged_in = is_plugged_in()
    while True:
        try:
            if plugged_in:
                plug_out_time = wait_for_unplug()
                print(f"plug_out_time: {convert_unix_time(plug_out_time)}")
                write_to_csv(plug_out_time, "Plug-out")
                plugged_in = False
                timer_start_time = time.time()
                timer_running = True
            else:
                plug_in_time = wait_for_plug()
                print(f"plug_in_time: {convert_unix_time(plug_in_time)}")
                write_to_csv(plug_in_time, "Plug-in")
                plugged_in = True
                timer_start_time = None
                timer_running = False

        except Exception as e:
            print(f"An error occurred: {str(e)}")


def is_plugged_in():
    battery = psutil.sensors_battery()
    return battery.power_plugged


def wait_for_plug():
    while True:
        if is_plugged_in():
            return int(time.time())
        time.sleep(1)


def wait_for_unplug():
    while True:
        if not is_plugged_in():
            return int(time.time())
        time.sleep(1)


def create_data_folder():
    folder_path = os.path.dirname(file_path)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def write_to_csv(time, event):
    create_data_folder()
    header = ["time", "action"]
    row = [time, event]

    file_exists = os.path.isfile(file_path)

    with open(file_path, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(header)

        writer.writerow(row)


def display_timer():
    global timer_start_time, timer_running
    while True:
        if timer_running:
            elapsed_time = time.time() - timer_start_time
            formatted_time = str(datetime.timedelta(seconds=int(elapsed_time)))
            print(f"Plugged out for: {formatted_time}\r", end="", flush=True)
        else:
            print(
                " " * 20, end="\r", flush=True
            )  # Clear the line if timer is not running
        time.sleep(1)


if __name__ == "__main__":
    record_thread = threading.Thread(target=record_plug_times)
    record_thread.start()

    timer_thread = threading.Thread(target=display_timer)
    timer_thread.start()

    input(f"Monitoring started at {datetime.datetime.now().isoformat()}\n")
