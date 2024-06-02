import asyncio
import logging
import csv
import fallAlgorithm as fa
from bleak import BleakClient, BleakScanner, BleakError
import matplotlib.pyplot as plt
from collections import deque

logging.basicConfig(level=logging.WARNING)

arduino_name = "Prototype_ArduinoNano2040"
service_uuid = "180D"
characteristic_uuid = "2A37"
csv_file_path = 'sensor_data'
file_num = 1



max_points = 100

timestamps = deque(maxlen=max_points)
aMag_values = deque(maxlen=max_points)
gMag_values = deque(maxlen=max_points)
ang_values = deque(maxlen=max_points)
bpm_values = deque(maxlen=max_points)



async def connect_to_device():
    devices = await BleakScanner.discover()
    for device in devices:
        if device.name == arduino_name:
            print(f"Found {arduino_name} with address {device.address}")
            return device.address
    raise Exception(f"{arduino_name} not found")

async def read_and_write_characteristic(address):
    try:
        async with BleakClient(address, timeout=20.0) as client:
            print(f"Connected to {arduino_name}")
            
            with open(csv_file_path+file_num+'.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                    
                file.seek(0, 2)  # Move to the end of the file
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
                    
                    aMag = fa.aceMag (aX, aY, aZ)
                    gMag = fa.gyroMag (gX, gY, gZ)
                    ang = fa.angle (aMag)

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
                    plt.pause(0.01)  # Pause briefly to update the plot3


                    if but == 1:
                        await client.write_gatt_char(characteristic_uuid, b'sos')
                        print("Sent: SOS!!!")
                    if but == 2:
                        await client.write_gatt_char(characteristic_uuid, b'fp')
                        print("Sent: False Positive")

                    await asyncio.sleep(1)
    except BleakError as e:
        print(f"Failed to connect: {e}")

async def main():
    address = await connect_to_device()
    await read_and_write_characteristic(address)

asyncio.run(main())
