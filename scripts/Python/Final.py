import asyncio
import logging
import csv
import fallAlgorithm as fa
from bleak import BleakClient, BleakScanner, BleakError
import matplotlib.pyplot as plt
from collections import deque
import firebase_admin
from firebase_admin import credentials, db, storage

logging.basicConfig(level=logging.WARNING)

arduino_name = "Prototype_ArduinoNano2040"
service_uuid = "180D"
characteristic_uuid = "2A37"
csv_directory = 'sensor_data/'
file_num = 1
counter = 0

max_points = 100

timestamps = deque(maxlen=max_points)
aMag_values = deque(maxlen=max_points)
gMag_values = deque(maxlen=max_points)
ang_values = deque(maxlen=max_points)
bpm_values = deque(maxlen=max_points)

plt.ion()

# Ensure 'sensor_data' directory exists
if not os.path.exists(csv_directory):
    os.makedirs(csv_directory)

# Firebase setup
cred = credentials.Certificate('/Users/pedro/Downloads/pic-2024-1bf68-firebase-adminsdk-nt7to-0f1c3b47dd.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://pic-2024-1bf68-default-rtdb.europe-west1.firebasedatabase.app/',
    'storageBucket': 'pic-2024-1bf68.appspot.com'
})

ref = db.reference('Values')
bucket = storage.bucket()

async def upload_csv_to_firebase(file_path, file_name):
    try:
        blob = bucket.blob(file_name)
        blob.upload_from_filename(file_path)
        print(f"Uploaded {file_name} to Firebase Storage.")
    except Exception as e:
        print(f"Failed to upload {file_name} to Firebase Storage: {e}")

async def connect_to_device():
    devices = await BleakScanner.discover()
    for device in devices:
        if device.name == arduino_name:
            print(f"Found {arduino_name} with address {device.address}")
            return device.address
    raise Exception(f"{arduino_name} not found")

async def read_and_write_characteristic(address):
    global file_num, counter
    while True:
        try:
            async with BleakClient(address, timeout=20.0) as client:
                print(f"Connected to {arduino_name}")
                
                current_minute = datetime.now().replace(second=0, microsecond=0)
                current_csv_filename = f"{current_minute.strftime('%Y-%m-%d_%H-%M')}.csv"
                csv_file_path = f"{csv_directory}{current_csv_filename}"

                with open(csv_file_path, mode='a', newline='') as file:
                    writer = csv.writer(file)

                    if file.tell() == 0:
                        writer.writerow(['Time', 'aMag', 'gMag', 'ang', 'bpm', 'but'])

                    while True:
                        # Read data from the characteristic
                        data = await client.read_gatt_char(characteristic_uuid)
                        print(f"Received: {data}")

                        decoded_data = data.decode('utf-8').strip()
                        print(f"Decoded: {decoded_data}")

                        # Parse the data
                        values = decoded_data.split(',')
                        timestamp = int(values[0])
                        aX = float(values[1])
                        aY = float(values[2])
                        aZ = float(values[3])
                        gX = float(values[4])
                        gY = float(values[5])
                        gZ = float(values[6])
                        bpm = float(values[7])
                        but = int(values[8])
                        
                        aMag = fa.aceMag(aX, aY, aZ)
                        gMag = fa.gyroMag(gX, gY, gZ)
                        ang = fa.angle(aMag)

                        writer.writerow([timestamp, aMag, gMag, ang, bpm, but])
                        print(f"Written to CSV: {timestamp}, {aMag, gMag, ang, bpm, but}")

                        # Append data to deque for plotting
                        timestamps.append(timestamp)
                        aMag_values.append(aMag)
                        gMag_values.append(gMag)
                        ang_values.append(ang)
                        bpm_values.append(bpm)

                        # Update the plot
                        plt.cla()
                        plt.plot(timestamps, aMag_values, label='aMag')
                        plt.plot(timestamps, gMag_values, label='gMag')
                        plt.plot(timestamps, ang_values, label='ang')
                        plt.plot(timestamps, bpm_values, label='bpm')
                        plt.xlabel('Time')
                        plt.ylabel('Magnitude')
                        plt.legend(loc='upper right')
                        plt.pause(0.01)  # Pause briefly to update the plot

                        # Send heart rate (bpm) to Firebase Realtime Database
                        ref.set({
                            'FellBolean': but,
                            'BPMM': 68,
                            'BPMW': 70,
                            'SLEEPH': "7 Hours",
                            'SLEEPQ': "80% quality",
                            'SleeparvgM': "7 Hours and 32 Minutes",
                            'SleepavrgW': "7 Hours and 15 Minutes",
                            'BPM': bpm
                        })
                        print(f"Sent to Firebase Realtime Database: {but}, {bpm}")

                        if but == 1:
                            await client.write_gatt_char(characteristic_uuid, b'sos')
                            print("Sent: SOS!!!")
                        if but == 2:
                            await client.write_gatt_char(characteristic_uuid, b'fp')
                            print("Sent: False Positive")

                        await asyncio.sleep(1)
                
                # Upload the current CSV file to Firebase Storage before creating a new one
                await upload_csv_to_firebase(csv_file_path, current_csv_filename)
                
                counter += 1
                if counter == 12:  
                    counter = 0
                    file_num += 1

        except (BleakError, EOFError) as e:
            print(f"Failed to connect or read data: {e}. Retrying in 5 seconds...")
            await asyncio.sleep(5)  # Wait for 5 seconds before retrying

async def main():
    address = await connect_to_device()
    await read_and_write_characteristic(address)

asyncio.run(main())
