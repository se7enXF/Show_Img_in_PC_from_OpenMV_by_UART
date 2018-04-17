# -*- coding: utf-8 -*
'''
 OpenMV串口发送程序
 By: se7en,凡哥
 2018年4月17日 11:33:00
 凡哥OpenMV广场QQ群：564048763
'''

import sensor,time,pyb
from pyb import UART

sensor.reset()
sensor.set_pixformat(sensor.RGB565) #GRAYSCALE
sensor.set_framesize(sensor.QQVGA)  #160*120
sensor.skip_frames()

uart = UART(3,921600,bits=8, parity=None, stop=1, timeout_char=1000,timeout=1000)
while(True):
    img = sensor.snapshot()                 #获取原始图片（RGB565或灰度）
    formate = img.format()                  #1（彩色）或3（灰度）
    pic = img.compress(quality=90)          #压缩后图片为jpeg格式

    uart.write("$7$"+str(pic.width()))      #原始图片宽度
    uart.write(str(pic.height()))           #原始图片高度
    uart.write(str(formate))                #原始图片格式
    uart.write(str(pic.size())+"\n")        #发送图片的字节数

    uart.write("$")                         #图片头帧
    uart.write(pic)                         #图片
    uart.write("$_$")                       #图片尾帧


