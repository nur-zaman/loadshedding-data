Load Shedding Monitoring Script
===============================

This script monitors the load shedding time using a laptop that is always connected to power. It records the plug-in and plug-out times during load shedding events and stores the data in a CSV file.

Usage
-----

1.  Clone the repository or download the script file.
2.  Make sure you have Python 3.x installed on your system.
3.  Run the script by double-clicking the `start_monitoring.bat` file or executing the following command in the terminal: `python monitor.py`.
4.  The script will start monitoring load shedding events and display the plug-out time when the power goes off, and the plug-in time when the power comes back.
5.  The recorded data will be stored in a CSV file named `plug_times.csv` in the same directory as the script.

**Note:** It is recommended to start the script while your laptop is plugged into a power source.

Disclaimer
----------

This script is intended for personal use and may not accurately reflect load shedding events in all regions. Please refer to official sources or power utility providers for the most accurate load shedding schedules.
