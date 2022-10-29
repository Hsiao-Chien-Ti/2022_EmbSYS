from bluepy.btle import Peripheral, UUID
from bluepy.btle import Scanner, DefaultDelegate
import time
class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)
    def handleNotification(self, cHandle, data):
        if cHandle==13:
            print("Heart rate: ",int.from_bytes(data, "big",signed=True))
        elif cHandle==19:
            print("MagnetoX: ",int.from_bytes(data, "big",signed=True))
        if cHandle==25:
            print("MagnetoY: ",int.from_bytes(data, "big",signed=True))
        if cHandle==31:
            print("MagnetoZ: ",int.from_bytes(data, "big",signed=True),'\n')
scanner = Scanner().withDelegate(ScanDelegate())
devices = scanner.scan (10.0)
n=0
addr = []
for dev in devices:
    print ("%d: Device %s (%s), RSSI=%d dB" % (n, dev.addr , dev.addrType , dev.rssi))
    addr.append(dev.addr)
    n += 1
    for (adtype , desc , value) in dev.getScanData():
        print (" %s = %s" % (desc ,value))
number = input('Enter your device number:')
print ('Device', number)
num= int (number)
print (addr[num])
print ("Connecting...")
dev = Peripheral(addr [num], 'random')
dev.setDelegate(ScanDelegate())
print ("Services...")
for svc in dev.services:
    print (str(svc))

testService = dev.getServiceByUUID (UUID(0x180D))
try:
    ch = dev.getCharacteristics(uuid =UUID(0x2A37))[0]
    cccd = ch.getHandle() + 1
    dev.writeCharacteristic(cccd, b"\x01\x00")
    chX = dev.getCharacteristics(uuid =UUID(0x1235))[0]
    cccd = chX.getHandle() + 1
    dev.writeCharacteristic(cccd, b"\x01\x00")
    chY = dev.getCharacteristics(uuid =UUID(0x1241))[0]
    cccd = chY.getHandle() + 1
    dev.writeCharacteristic(cccd, b"\x01\x00")
    chZ = dev.getCharacteristics(uuid =UUID(0x1247))[0]
    cccd = chZ.getHandle() + 1
    dev.writeCharacteristic(cccd, b"\x01\x00")

    while 1:
        if dev.waitForNotifications(1.0):
            continue

finally:
    dev.disconnect()
