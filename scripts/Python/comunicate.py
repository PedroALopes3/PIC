import asyncio
import logging
import fallAlgorithm
from bleak import BleakClient, BleakScanner, BleakError

logging.basicConfig(level=logging.WARNING)

arduino_name = "Prototype_ArduinoNano2040"
service_uuid = "180D"
characteristic_uuid = "2A37"

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

            while True:
                # Read data from the characteristic
                data = await client.read_gatt_char(characteristic_uuid)
                print(f"Received: {data}")

                # Send a hello message
                await client.write_gatt_char(characteristic_uuid, b'Hello from Python')
                print("Sent: Hello from Python")

                await asyncio.sleep(1)
    except BleakError as e:
        print(f"Failed to connect: {e}")

async def main():
    address = await connect_to_device()
    await read_and_write_characteristic(address)

asyncio.run(main())
