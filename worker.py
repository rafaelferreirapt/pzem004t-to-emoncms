#!/usr/bin/env python3
# coding=utf-8

import serial
import time
import struct
import requests
import json
from airbrake.notifier import Airbrake

with open('config.json') as f:
    CONFIG = json.load(f)

ab = Airbrake(host=CONFIG["ERRBIT_HOST"],
              api_key=CONFIG["ERRBIT_PROJECT_KEY"],
              project_id=CONFIG["ERRBIT_PROJECT_ID"])


class BTPOWER:
    setAddrBytes = [0xB4, 0xC0, 0xA8, 0x01, 0x01, 0x00, 0x1E]
    readVoltageBytes = [0xB0, 0xC0, 0xA8, 0x01, 0x01, 0x00, 0x1A]
    readCurrentBytes = [0XB1, 0xC0, 0xA8, 0x01, 0x01, 0x00, 0x1B]
    readPowerBytes = [0XB2, 0xC0, 0xA8, 0x01, 0x01, 0x00, 0x1C]
    readRegPowerBytes = [0XB3, 0xC0, 0xA8, 0x01, 0x01, 0x00, 0x1D]

    def __init__(self, com="/dev/tty.usbserial", timeout=10.0):
        self.ser = serial.Serial(
            port=com,
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=timeout
        )
        if self.ser.isOpen():
            self.ser.close()
        self.ser.open()

    def checkChecksum(self, _tuple):
        _list = list(_tuple)
        _checksum = _list[-1]
        _list.pop()
        _sum = sum(_list)

        if _checksum == _sum % 256:
            return True
        else:
            raise Exception("Wrong checksum")

    def isReady(self):
        self.ser.write(serial.to_bytes(self.setAddrBytes))

        rcv = self.ser.read(7)

        if len(rcv) == 7:
            unpacked = struct.unpack("!7B", rcv)

            if self.checkChecksum(unpacked):
                return True
        else:
            raise serial.SerialTimeoutException("Timeout setting address")

    def readVoltage(self):
        self.ser.write(serial.to_bytes(self.readVoltageBytes))
        rcv = self.ser.read(7)

        if len(rcv) == 7:
            unpacked = struct.unpack("!7B", rcv)

            if self.checkChecksum(unpacked):
                tension = unpacked[2] + unpacked[3] / 10.0
                return tension
        else:
            raise serial.SerialTimeoutException("Timeout reading tension")

    def readCurrent(self):
        self.ser.write(serial.to_bytes(self.readCurrentBytes))
        rcv = self.ser.read(7)

        if len(rcv) == 7:
            unpacked = struct.unpack("!7B", rcv)

            if self.checkChecksum(unpacked):
                return unpacked[2] + unpacked[3] / 100.0
        else:
            raise serial.SerialTimeoutException("Timeout reading current")

    def readPower(self):
        self.ser.write(serial.to_bytes(self.readPowerBytes))
        rcv = self.ser.read(7)

        if len(rcv) == 7:
            unpacked = struct.unpack("!7B", rcv)

            if self.checkChecksum(unpacked):
                return unpacked[1] * 256 + unpacked[2]
        else:
            raise serial.SerialTimeoutException("Timeout reading power")

    def readRegPower(self):
        self.ser.write(serial.to_bytes(self.readRegPowerBytes))
        rcv = self.ser.read(7)

        if len(rcv) == 7:
            unpacked = struct.unpack("!7B", rcv)

            if self.checkChecksum(unpacked):
                return unpacked[1] * 256 * 256 + unpacked[2] * 256 + unpacked[3]
        else:
            raise serial.SerialTimeoutException("Timeout reading registered power")

    def readAll(self):
        return self.readCurrent(), self.readPower()

    def close(self):
        self.ser.close()


if __name__ == "__main__":

    try:
        sensor = BTPOWER()

        if sensor.isReady():
            # init message
            print("Reading and sending to emoncms...")
            ab.notify("Reading and sending to emoncms...")

            while True:
                current, power = sensor.readAll()

                json_inputs = json.dumps({
                    'current': str(current),
                    'power': str(power)
                })

                payload = {'apikey': CONFIG["API_KEY"], 'fulljson': json_inputs, 'node': 'emontx'}

                requests.get(CONFIG["HOST"] + "/emoncms/input/post", params=payload)

                time.sleep(1)
    except Exception:
        ab.capture()

