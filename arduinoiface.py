import serial
import threading
import numpy


class DoubleVarContainer:
    def __init__(self, container):
        self.container = container

    def update(self, value):
        self.container.set(value)


class Reader:
    def __init__(self, port):
        try:
            self.arduino = serial.Serial(port, 9600, timeout=.1)
            print("ARDUINO CONECTADO")
        except serial.serialutil.SerialException:
            print("[ERROR] No se pudo conectar con el arduino.")
            exit(1)
        #self.dvar = DoubleVarContainer(dvar)
        self.t = None
        self.value = []
        #self.measures = [0 for i in range(int(size))]

    def start(self):
        self.t = threading.Thread(target=self.__read)
        self.t.daemon = True
        self.t.start()

    def bytes_to_int(self,bytes):
        result = 0
        for b in bytes:
            result = result * 256 + int(b)
        return result

    def ascii_to_int(self):
        self.value.pop()
        self.value.pop()
        print(self.value)
        v = ''.join(map(chr,self.value))
        
        return int(v)

    def read(self):
        resolution = 100 / 255
        data = self.arduino.read(1)
        if data:
            a = self.bytes_to_int(data) 
            self.value.insert(len(self.value),a)
        else:
            if len(self.value) > 0:
                com_bin = self.ascii_to_int()
                self.value = []  
                return com_bin
            else:
                self.value = []  
                return -1
            
                
