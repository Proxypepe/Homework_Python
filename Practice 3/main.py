import struct

def f31(x):
    res = {'A1': struct.unpack('b', x[5:6])[0], 'A2': struct.unpack('>Q', x[6:14])[0],
           'A3': struct.unpack('b', x[14:15])[0], 'A4': []}
    for i in range(2):
        res['A4'].append({})
        res['A4'][i]['B1'] = struct.unpack('>i', x[15 + 17 * i: 19 + 17 * i])[0]
        res['A4'][i]['B2'] = struct.unpack('>d', x[19 + 17 * i: 27 + 17 * i])[0]
        res['A4'][i]['B3'] = struct.unpack('>f', x[27 + 17 * i: 31 + 17 * i])[0]
        res['A4'][i]['B4'] = struct.unpack('B', x[31 + 17 * i: 32 + 17 * i])[0]
    # index 49
    addr_C = struct.unpack('>H', x[49:51])[0]
    res['A5'] = {}
    res['A5']['C1'] = ''
    size = struct.unpack(">I", x[addr_C: addr_C + 4])[0]
    addr = struct.unpack(">I", x[addr_C + 4: addr_C + 8])[0]
    # Адрес(uint16) структуры C
    for i in range(addr, addr + size):
        res['A5']['C1'] += chr(x[i])
    res['A5']['C2'] = []
    for i in range(3):
        elem = struct.unpack('>h', x[addr_C + 8 + 2 * i: addr_C + 10 + 2 * i])[0]
        res['A5']['C2'].append(elem)
    res['A5']['C3'] = struct.unpack(">Q", x[addr_C + 14: addr_C + 22])[0]
    res['A5']['C4'] = {}
    res['A5']['C4']['D1'] = struct.unpack(">Q", x[addr_C + 22: addr_C + 30])[0]
    res['A5']['C4']['D2'] = struct.unpack(">I", x[addr_C + 30: addr_C + 34])[0]
    res['A5']['C4']['D3'] = struct.unpack(">i", x[addr_C + 34: addr_C + 38])[0]
    res['A5']['C4']['D4'] = struct.unpack(">b", x[addr_C + 38: addr_C + 39])[0]
    res['A5']['C5'] = struct.unpack(">B", x[addr_C + 39: addr_C + 40])[0]
    res['A5']['C6'] = []
    res['A5']['C7'] = []
    for i in range(2):
        elem = struct.unpack('>h', x[addr_C + 40 + 2 * i: addr_C + 42 + 2 * i])[0]
        res['A5']['C6'].append(elem)
    for i in range(4):
        elem = struct.unpack('>B', x[addr_C + 44 + 1 * i: addr_C + 45 + 1 * i])[0]
        res['A5']['C7'].append(elem)
    res['A6'] = struct.unpack('>d', x[51: 59])[0]
    res['A7'] = struct.unpack('>Q', x[59: 67])[0]

    return res


class C32:
    def __init__(self):
        self.position = 'A'

    def slip(self):
        if self.position == 'A':
            self.position = 'B'
            return 0
        elif self.position == 'B':
            self.position = 'C'
            return 1
        elif self.position == 'C':
            self.position = 'D'
            return 3
        elif self.position == 'E':
            self.position = 'C'
            return 7
        elif self.position == 'F':
            self.position = 'G'
            return 8
        elif self.position == 'G':
            self.position = 'C'
            return 11
        else:
            raise RuntimeError()

    def hop(self):
        if self.position == 'B':
            return 2
        elif self.position == 'E':
            self.position = 'F'
            return 6
        elif self.position == 'F':
            self.position = 'B'
            return 9

        else:
            raise RuntimeError()

    def join(self):
        if self.position == 'D':
            self.position = 'H'
            return 5
        elif self.position == 'G':
            self.position = 'H'
            return 10
        else:
            raise RuntimeError()

    def rev(self):
        if self.position == 'D':
            self.position = 'E'
            return 4
        else:
            raise RuntimeError()
