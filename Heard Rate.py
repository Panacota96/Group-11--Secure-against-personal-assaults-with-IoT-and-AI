#ADDRESS = "XX:XX:XX:XX:XX:XX"  # Dirección MAC del PineTime
#CHARACTERISTIC_UUID = "00002a37-0000-1000-8000-00805f9b34fb"  # UUID del ritmo cardíaco (Heart Rate Measurement)

from bleak import BleakClient

async def read_heart_rate():
    async with BleakClient(ADDRESS) as client:
        def callback(sender, data):
            print(f"Heart rate data: {data}")

        await client.start_notify(CHARACTERISTIC_UUID, callback)
        await asyncio.sleep(30)  # Tiempo de lectura

asyncio.run(read_heart_rate())

def detect_anomaly(bpm):
    if bpm > 120 or bpm < 50:
        return True
    return False
# Ejemplo de uso
bpm = 100
if detect_anomaly(bpm):
    print("Anomaly detected!")
else:
    print("No anomaly detected.")