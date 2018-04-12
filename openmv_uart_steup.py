# -*- coding: utf-8 -*
# By: se7en - 周三 四月 11 2018

import sensor,time,pyb
from pyb import UART

sensor.reset()
sensor.set_pixformat(sensor.RGB565) #GRAYSCALE
sensor.set_framesize(sensor.QQVGA)  #160*120
sensor.skip_frames()
#clock = time.clock()

uart = UART(3,115200,bits=8, parity=None, stop=1, timeout_char=1000,timeout=1000)

while(True):
    #clock.tick()
    img = sensor.snapshot()                 #获取原始图片（RGB565或灰度）
    formate = img.format()
    pic = img.compress(quality=80)          #压缩后图片为jpeg格式
    #print(pic)

    uart.write("$7$"+str(pic.width()))      #160
    uart.write(str(pic.height()))           #120
    uart.write(str(formate))                #1（彩色）或3（灰度）
    uart.write(str(pic.size())+"\n")        #发送图片的字节数

    #print("Start......")
    uart.write("$")                         #图片头帧
    uart.write(pic)                         #图片
    uart.write("$_$")                       #图片尾帧
    #print("Done.......")
    #print(clock.fps())

