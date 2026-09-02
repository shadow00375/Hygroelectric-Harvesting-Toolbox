import serial
import csv
import time
from datetime import datetime

# --- CONFIGURATION ---
PORT = 'COM6' #Check your device manager for the correct COM port
BAUD_RATE = 9600
CSV_FILE = f'{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}_log.csv'# Not sure of this works. Use the bottom line if it doesn't XD
# CSV_FILE = 'data_log.csv'

def main():
    try:
        # Establish serial connection on COM6
        ser = serial.Serial(PORT, BAUD_RATE, timeout=2)
        print(f"Successfully connected to {PORT} at {BAUD_RATE} baud.")
        
        # Give connection time to initialize
        time.sleep(2)

        # Open CSV file in append mode
        with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            
            # Write column header if creating a new file
            if file.tell() == 0:
                writer.writerow(['Timestamp', 'Data'])
                file.flush()

            print(f"Logging data to '{CSV_FILE}'... Press Ctrl+C to stop.\n" + "=" * 50)

            while True:
                # Check if there is data waiting in the buffer
                if ser.in_waiting > 0:
                    # Read line until newline '\n' character
                    raw_data = ser.readline()
                    
                    try:
                        # Decode raw bytes into a string and strip extra whitespace/newlines
                        data_str = raw_data.decode('utf-8', errors='replace').strip()
                        
                        if data_str:
                            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                            
                            # Write row to CSV
                            writer.writerow([timestamp, data_str])
                            file.flush()  # Force write to disk immediately
                            
                            # Display on console
                            print(f"[{timestamp}] {data_str}")
                            
                    except Exception as e:
                        print(f"Error processing line: {e}")
                
                # Small pause to prevent CPU spiking
                time.sleep(0.01)

    except serial.SerialException as e:
        print(f"\nSerial Error on {PORT}: {e}")
        print("Tip: Make sure no other program (like Arduino IDE Serial Monitor) is using COM6.")
    except KeyboardInterrupt:
        print("\nLogging stopped by user.")
    finally:
        if 'ser' in locals() and ser.is_open:
            ser.close()
            print("Port COM6 closed.")

if __name__ == '__main__':
    main()
