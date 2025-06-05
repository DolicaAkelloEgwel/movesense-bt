import asyncio
from bleak import BleakScanner, BleakClient

def _find_movesense(devices):
    for d in devices:
        if "Movesense" in d.name:
            return d.address
    return ""

async def main():
    devices = await BleakScanner.discover()
    ADDRESS = _find_movesense(devices)
    if not ADDRESS:
        print("Can't connect to Movesense")
        exit()

    async with BleakClient(ADDRESS) as client:
        model_number = await client.read_gatt_char(MODEL_NBR_UUID)
        print("Model Number: {0}".format("".join(map(chr, model_number))))

asyncio.run(main())
