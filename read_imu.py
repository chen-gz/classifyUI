def twos_comp(val, bits):
    """compute the 2's complement of int value val"""
    if (val & (1 << (bits - 1))) != 0:  # if sign bit is set e.g., 8bit: 128-255
        val = val - (1 << bits)  # compute negative value
    return val


class imu:
    def __init__(self):
        i = 0

    def setpath(self,path):
        self.path = path

    def processImuData(self):
        self.timestamp = []
        self.acc = []  # Acceleration
        self.gyro = []  # Gyroscope
        self.mag = []  # Magnetometer
        with open(self.path, 'rb') as f:
            while (1):
                samplePoint = []
                eof = f.tell()
                for i in range(24):
                    byte = f.read(1)
                    samplePoint.append(int.from_bytes(byte, 'little'))
                if len(samplePoint) != 24 or eof == f.tell():
                    break
                # hour minutes sec
                self.timestamp.append([samplePoint[0], samplePoint[3], samplePoint[2]])
                #  timestamp = (samplePoint[3] << 8) + samplePoint[2]
                #  timestamp_min = timestamp >> 8
                #  timestamp_sec = timestamp % 256

                acc1 = twos_comp((samplePoint[5] << 8) + samplePoint[4], 16)
                acc2 = twos_comp((samplePoint[7] << 8) + samplePoint[6], 16)
                acc3 = twos_comp((samplePoint[9] << 8) + samplePoint[8], 16)
                self.acc.append([acc1, acc2, acc3])

                gyro1 = twos_comp((samplePoint[13] << 8) + samplePoint[12], 16) / 10
                gyro2 = twos_comp((samplePoint[15] << 8) + samplePoint[14], 16) / 10
                gyro3 = twos_comp((samplePoint[17] << 8) + samplePoint[16], 16) / 10
                self.gyro.append([gyro1, gyro2, gyro3])

                mag1 = twos_comp((samplePoint[19] << 8) + samplePoint[18], 16) / 10
                mag2 = twos_comp((samplePoint[21] << 8) + samplePoint[20], 16) / 10
                mag3 = twos_comp((samplePoint[23] << 8) + samplePoint[22], 16) / 10
                self.mag.append([mag1, mag2, mag3])
