import asyncio
import logging
import csv
import random
import time
from datetime import datetime, timedelta
import os
import matplotlib.pyplot as plt
from collections import deque
import firebase_admin
from firebase_admin import credentials, db, storage

logging.basicConfig(level=logging.WARNING)

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
cred = credentials.Certificate('/Users/pedro/Downloads/pic24-cfe9a-firebase-adminsdk-mddbb-3a74be8200.json') 
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://pic24-cfe9a-default-rtdb.europe-west1.firebasedatabase.app/',  
    'storageBucket': 'pic24-cfe9a.appspot.com'  
})


ref = db.reference('heart_rate')

bucket = storage.bucket()

async def upload_csv_to_firebase(file_path, file_name):
    try:
        blob = bucket.blob(file_name)
        blob.upload_from_filename(file_path)
        print(f"Uploaded {file_name} to Firebase Storage.")
    except Exception as e:
        print(f"Failed to upload {file_name} to Firebase Storage: {e}")

async def generate_random_data():
    global file_num, counter
    while True:
        try:
            current_minute = datetime.now().replace(second=0, microsecond=0)
            current_csv_filename = f"{current_minute.strftime('%Y-%m-%d_%H-%M')}.csv"
            csv_file_path = f"{csv_directory}{current_csv_filename}"  # Update CSV file path
            
            with open(csv_file_path, mode='a', newline='') as file:
                writer = csv.writer(file)

                if file.tell() == 0:
                    writer.writerow(['Time', 'aMag', 'gMag', 'ang', 'bpm', 'but'])

                # Log data every 5 seconds within current minute
                start_time = time.time()
                while time.time() - start_time <= 60:  # Run for one minute
                    # Generate random data
                    timestamp = int(time.time())
                    aX = random.uniform(-10, 10)
                    aY = random.uniform(-10, 10)
                    aZ = random.uniform(-10, 10)
                    gX = random.uniform(-500, 500)
                    gY = random.uniform(-500, 500)
                    gZ = random.uniform(-500, 500)
                    bpm = random.uniform(60, 100)
                    but = random.randint(0, 2)

                    aMag = (aX**2 + aY**2 + aZ**2)**0.5
                    gMag = (gX**2 + gY**2 + gZ**2)**0.5
                    ang = random.uniform(0, 180)

                    writer.writerow([timestamp, aMag, gMag, ang, bpm, but])
                    print(f"Written to CSV: {timestamp}, {aMag}, {gMag}, {ang}, {bpm}, {but}")

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
                    ref.push({
                        'timestamp': timestamp,
                        'bpm': bpm
                    })
                    print(f"Sent to Firebase Realtime Database: {timestamp}, {bpm}")

                    if but == 1:
                        print("Button pressed: SOS!!!")
                    elif but == 2:
                        print("Button pressed: False Positive")

                    await asyncio.sleep(1)  

               
                await upload_csv_to_firebase(csv_file_path, current_csv_filename)
                
                counter += 1
                if counter == 12:  
                    counter = 0
                    file_num += 1

        except Exception as e:
            print(f"An error occurred: {e}. Retrying in 5 seconds...")
            await asyncio.sleep(5)  # Wait for 5 seconds before retrying

async def main():
    await generate_random_data()

asyncio.run(main())
