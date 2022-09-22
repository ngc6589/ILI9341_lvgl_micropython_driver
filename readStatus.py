def readValue(cmd, len):
    cs.value(0)
    dc.value(0)
    spi.write(bytes([cmd]))
    dc.value(1)
    result=spi.read(len)
    cs.value(1)
    return result

def printValue(disp, cmd, len):
    result = readValue(cmd, len)
    print(disp, end=" ")
    for i in result:
        print(hex(i), end=" ")
    print()


cs = machine.Pin(9, mode=machine.Pin.OUT, value=1)
dc = machine.Pin(8, mode=machine.Pin.OUT, value=1)
spi = machine.SPI(
    1,
    baudrate = 10_000,
    polarity = 0,
    phase = 0,
    bits = 8,
    firstbit = machine.SPI.MSB,
    sck  = machine.Pin(10, mode=machine.Pin.OUT),
    mosi = machine.Pin(11, mode=machine.Pin.OUT),
    miso = machine.Pin(12, mode=machine.Pin.IN)
)
printValue("Display Identification              0x04: ", 0x04, 4)
printValue("Display Status                      0x09: ", 0x09, 5)
printValue("Display Power Mode                  0x0A: ", 0x0A, 2)
printValue("Display MADCTL                      0x0B: ", 0x0B, 2)
printValue("Display Pixel Format                0x0C: ", 0x0C, 2)
printValue("Display Image Format                0x0D: ", 0x0D, 2)
printValue("Display Signal Format               0x0E: ", 0x0E, 2)
printValue("Display Self-Diag Result            0x0F: ", 0x0F, 2)
printValue("Display Brightness                  0x52: ", 0x52, 2)
printValue("Content Adaptive Brightness Control 0x56: ", 0x56, 2)
printValue("CABC Minimum Brightness             0x5F: ", 0x5F, 2)
printValue("Read ID1                            0xDA: ", 0xDA, 2)
printValue("Read ID2                            0xDB: ", 0xDB, 2)
printValue("Read ID3                            0xDC: ", 0xDC, 2)
printValue("Read ID4                            0xD3: ", 0xD3, 4)
