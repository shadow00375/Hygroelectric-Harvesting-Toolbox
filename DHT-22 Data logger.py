import serial
import csv
from datetime import datetime

SERIAL_PORT = 'COM4'      # Change to your Arduino's port
BAUD_RATE = 9600

input("Press Enter to start logging...")   # Synchronised manual start
start_time = datetime.now()
print(f"Logging started at {start_time.isoformat()}")

start_time_str = start_time.strftime('%Y-%m-%d_%H-%M-%S')
OUTPUT_FILE = f'sensor_log_{start_time_str}.csv'

ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=2)

with open(OUTPUT_FILE, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['time', 'temperature', 'humidity'])  # header

    print(f"Logging to {OUTPUT_FILE}. Press CTRL+C to stop.")
    try:
        while True:
            line = ser.readline().decode('utf-8').strip()
            if not line or line.startswith('err'):
                continue  # skip empty or error lines

            parts = line.split(',')
            if len(parts) != 2:
                continue  # skip malformed lines

            try:
                temp = float(parts[0])
                hum = float(parts[1])
            except ValueError:
                continue

            Time = datetime.now().isoformat()  # e.g., 2026-07-13T14:35:22
            writer.writerow([Time, temp, hum])
            f.flush()  # ensure data is written immediately
            print(f"{Time}  Temp: {temp}°C  Hum: {hum}%")

    except KeyboardInterrupt:
        print("\nLogging stopped.")