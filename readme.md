# LVGL Micropython 用 ILI9341 汎用ドライバ
Micropython bindings to LVGL for Embedded devices, Unix and JavaScript https://github.com/lvgl/lv_micropython の Raspberry Pi Pico 用 ILI9341 汎用ドライバです。

# 参考資料  
eudoxos さん (https://github.com/eudoxos) 作成の ST7789 用ドライバを修正して作成しました。MITライセンスで公開されていますので、こちらのファイルも MIT ライセンスとします。  
https://github.com/lvgl/lv_binding_micropython/blob/master/driver/generic/st77xx.py  
https://github.com/lvgl/lv_binding_micropython/blob/master/driver/generic/xpt2046.py  

また、Adafruit 社が公開されている ILI9341 のコードを参考にしてコーディングしています。
https://github.com/adafruit/Adafruit_ILI9341/blob/master/Adafruit_ILI9341.h  
https://github.com/adafruit/Adafruit_ILI9341/blob/master/Adafruit_ILI9341.cpp  

# 制限
このドライバは http://www.lcdwiki.com/2.8inch_SPI_Module_ILI9341_SKU:MSP2807 LCD Wiki にある、2.8inch SPI Module ILI9341 SKU:MSP2807 という液晶で動作を確認しました。それ以外の液晶で動作するかわかりません。  
DMA はサポート出来ていません。コメントアウトしてます。


# ILI9341 Generic Driver for LVGL Micropython
ILI9341 Generic Driver for Raspberry Pi Pico in Micropython bindings to LVGL for Embedded devices, Unix and JavaScript https://github.com/lvgl/lv_micropython .

# References  
This is a modified version of the driver for ST7789 by eudoxos (https://github.com/eudoxos). Since it is released under MIT license, this file is also MIT licensed.  
https://github.com/lvgl/lv_binding_micropython/blob/master/driver/generic/st77xx.py  
https://github.com/lvgl/lv_binding_micropython/blob/master/driver/generic/xpt2046.py  

I also coded the code based on ILI9341 code released by Adafruit.
https://github.com/adafruit/Adafruit_ILI9341/blob/master/Adafruit_ILI9341.h  
https://github.com/adafruit/Adafruit_ILI9341/blob/master/Adafruit_ILI9341.cpp  

# Limitations
This driver has been tested with the LCD named 2.8inch SPI Module ILI9341 SKU:MSP2807 from http://www.lcdwiki.com/2.8inch_SPI_Module_ILI9341_SKU:MSP2807 LCD Wiki. I do not know if it works on other LCDs.  
DMA is not supported. Commented out.

Translated with www.DeepL.com/Translator (free version)