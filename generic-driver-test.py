import sys
sys.path.append('.')
import MSP2807_ILI9341
import MSP2807_XPT2046
import rp2_dma

spi=machine.SPI(
    1,
    baudrate=40_000_000,
    polarity=0,
    phase=0,
    sck=machine.Pin(10,machine.Pin.OUT),
    mosi=machine.Pin(11,machine.Pin.OUT),
    miso=machine.Pin(12,machine.Pin.IN)
)        

dma0=rp2_dma.DMA(1)

lcd = MSP2807_ILI9341.ILI9341(
    rot=MSP2807_ILI9341.PORTRAIT,
    res=(240,320),
    spi=spi,
    cs=9,
    dc=8,
    bl=13,
    rst=15,
    doublebuffer=True,
#    doublebuffer=False,
    bgr=False,
    rp2_dma=dma0
)
lcd.set_backlight(100)

spi2 = machine.SoftSPI(
    baudrate=1_000_000,
    polarity=0,
    phase=0,
    sck =machine.Pin(17,machine.Pin.OUT),
    mosi=machine.Pin(18,machine.Pin.OUT),
    miso=machine.Pin(19,machine.Pin.IN)
)
touch = MSP2807_XPT2046.Xpt2046(spi=spi2,cs=16,rot=MSP2807_XPT2046.PORTRAIT)

import lvgl as lv
lv.init()

lcd.set_backlight(30)

scr=lv.obj()
btn=lv.btn(scr)
lbl=lv.label(btn)
lbl.set_text("Press me!")
btn.center()
btn.add_event(lambda event: print('Button clicked!'),lv.EVENT.CLICKED,None)
lv.scr_load(scr)
